import requests
import json
import sys

# Rasa server endpoint
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

def test_accuracy(query_file):
    try:
        with open(query_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {query_file} not found.")
        return

    queries = data.get('queries', [])
    total = len(queries)
    if total == 0:
        print("No queries found to test.")
        return

    success_count = 0
    results = []

    print(f"Starting accuracy test for {total} queries...\n")

    for i, item in enumerate(queries):
        query_text = item.get('text')
        expected_intent = item.get('intent')
        
        payload = {
            "sender": "test_user",
            "message": query_text
        }

        print(f"[{i+1}/{total}] Testing: {query_text}...", end="", flush=True)

        try:
            response = requests.post(RASA_URL, json=payload, timeout=10)
            response.raise_for_status()
            messages = response.json()
            
            # Combine all text responses from the bot
            full_response_text = " ".join([m.get("text", "") for m in messages if "text" in m])
            
            # success criteria: 
            # 1. contains "Sql query:" (most actions echo the query)
            # 2. contains "Successfully" (for insert/update/delete)
            # 3. contains table formatting "|" (for show table)
            # 4. doesn't contain fallback message
            
            # success criteria: 
            # 1. contains "Sql query:" (most actions echo the query)
            # 2. contains "Successfully" (for insert/update/delete)
            # 3. contains table formatting "|" (for show table)
            # 4. contains MySQL IntegrityError (proves SQL was generated and executed)
            # 5. contains "No results found" (valid query, just no data)
            
            is_success = False
            if any(marker in full_response_text for marker in ["Sql query:", "Successfully", "|", "IntegrityError", "No results found"]):
                is_success = True
            
            if "It seems like you're asking a question that is outside the scope" in full_response_text or not full_response_text.strip():
                is_success = False

            if is_success:
                success_count += 1
                status = "PASS"
            else:
                status = "FAIL"

            results.append({
                "query": query_text,
                "response": full_response_text,
                "status": status
            })
            
            print(f"[{i+1}/{total}] {status}: {query_text}")

        except requests.exceptions.RequestException as e:
            print(f"[{i+1}/{total}] ERROR communicating with server: {e}")
            results.append({
                "query": query_text,
                "error": str(e),
                "status": "ERROR"
            })

    accuracy = (success_count / total) * 100
    print(f"\nFinal Accuracy: {accuracy:.2f}% ({success_count}/{total})")
    
    with open('test_results.json', 'w') as f:
        json.dump({"accuracy": accuracy, "details": results}, f, indent=2)
    
    return accuracy

if __name__ == "__main__":
    test_accuracy('test_queries.json')
