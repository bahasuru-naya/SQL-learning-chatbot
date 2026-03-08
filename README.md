# SQL Learning Assistant Chatbot

<img width="1608" height="862" alt="image" src="https://github.com/user-attachments/assets/c6ab4cdd-75ae-4fa8-9334-570a156dd995" />

## Overview
**SQL Learning Assistant Chatbot** is an AI-powered chatbot designed to help students and developers learn SQL through interactive, natural language conversations. Built with the **Rasa framework**, it translates user intents into real-time database operations, allowing users to practice CRUD (Create, Read, Update, Delete) actions and data analysis without needing to write complex SQL syntax manually.

The assistant provides a modern, user-friendly interface with integrated voice Support, making the learning experience both dynamic and accessible.

---

##  Key Features
- **Natural Language to SQL**: Interactively query the database using plain English.
- **Real-time Database Interaction**: Perform `SELECT`, `INSERT`, `UPDATE`, and `DELETE` operations directly through the chat.
- **Advanced Data Analysis**: Ask for insights like "show details about sales of each item" and get formatted tabular results.
- **Voice-Enabled Learning**: Built-in **Speech-to-Text** and **Text-to-Speech** (Voice) capabilities for hands-free interaction.
- **Modern Dashboard**: Responsive web interface with:
  - **Dark Mode** support for comfortable viewing.
  - **Database Schema Visualization** to understand table structures.
  - **Smart Suggestions** to help users get started with common commands.

---

## Architecture & Tech Stack

###  Backend (Logic & NLU)
- **Rasa Open Source**: Manages Natural Language Understanding (NLU) and dialogue policies.
- **Python SDK (rasa-sdk)**: Handles custom actions for database connectivity.
- **SQLAlchemy**: ORM used to interface with the MySQL database.

###  Frontend (User Interface)
- **HTML5 & Vanilla CSS**: Premium, responsive UI design.
- **JavaScript (ES6+)**: Handles real-time DOM updates and voice processing.
- **Socket.io**: Enables low-latency, bi-directional communication between the UI and Rasa server.

###  Database
- **MySQL**: Persistent storage for stock, prices, and sales data.

---

## Setup & Installation

### 1. Prerequisites
- Python 3.7.6 
- MySQL Server

### 2. Database Configuration
1. Create a MySQL database named `csitem`.
2. Ensure your credentials match those in `actions/actions.py` (default: `username: 'root'`, `password: 'password'`).
3. Set up your tables (e.g., `stock`, `price`, `sales`).

### 3. Backend Setup
Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 4. Training the Model
Before running the assistant for the first time or after making changes to the training data, you must train the models:
```bash
rasa train
```

### 5. Running the Assistant
You need to run the Rasa server and the Action server concurrently.

**Start Rasa Server:**
```bash
rasa run --enable-api --cors "*"
```

**Start Custom Actions Server:**
```bash
rasa run actions
```

### 6. Frontend Deployment
Simply open `Frontend/index.html` in your web browser. Ensure the Rasa server is running on `http://localhost:5005`.

---

## Testing

### 1. Rasa Built-in Testing (E2E)
The assistant includes end-to-end test stories to ensure dialogue flows and intent classifications remain consistent.
- **Test File**: `tests/test_stories.yml`
- **Run Tests**:
  ```bash
  rasa test
  ```

### 2. Custom SQL Query Accuracy Testing
To ensure the chatbot accurately translates natural language into successful database operations, a dedicated accuracy test suite is provided.
- **Location**: `tests/sql-query-accuracy-test/`
- **Components**:
  - `test_queries.json`: A dataset of 100 diverse natural language queries covering all supported intents (CRUD and joins).
  - `test_accuracy.py`: An automated script that validates the bot's responses via the Rasa REST API.
- **Status**: The assistant maintains a **90.00% accuracy** score across the 100-query benchmark.
- **Run Accuracy Test**:
  Ensure the Rasa and Action servers are running, then execute:
  ```powershell
  python tests/sql-query-accuracy-test/test_accuracy.py
  ```

---

##  Dataset & Research
This project includes a comprehensive NLU dataset (located in `data/`) designed for training SQL learning assistants.
- **500+ Examples**: Diverse phrasing for intent classification and entity recognition.
- **Annotated Entities**: Extracts table names, quantities, IDs, and conditions from user queries.
- **Lookup Tables**: Enhances recognition of domain-specific SQL terminology.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


