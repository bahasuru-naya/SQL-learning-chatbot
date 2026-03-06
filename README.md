# Dataset Documentation

## Overview
This dataset was developed to train and evaluate the Natural Language Understanding (NLU) component of an AI-powered SQL learning chatbot implemented using the **Rasa framework**. The dataset is structured according to the **Rasa YAML training data specification** and supports tasks such as **intent classification**, **entity recognition**, and **semantic mapping of natural language queries to database operations**.

The dataset was designed to capture a wide variety of natural language expressions that students may use when interacting with a SQL learning assistant.

## Dataset Design
The dataset consists of annotated natural language training examples organized into multiple intents that represent different categories of user queries. Each intent corresponds to a specific SQL-related operation or learning query.

To improve model generalization and linguistic coverage, **distinct examples** were created for each intent. These examples include variations in:

- Sentence structure  
- Lexical choices and synonyms  
- Query phrasing styles  
- Parameter ordering within queries  

**Overall, more than 500 distinct training examples were created across all intents**, ensuring sufficient diversity and coverage of possible user expressions.

This diversity enables the NLU model to recognize semantically equivalent queries expressed in different linguistic forms.

## Annotation Structure

### Intents
Intents represent the **user’s underlying goal** in a query. Examples include requests to retrieve data, apply filtering conditions, or perform SQL-related operations. Each intent contains multiple annotated training examples to support robust classification.

### Entities
Entities are annotated within the natural language examples to identify parameters necessary for query construction. These entities typically correspond to structured database components such as:

- Table names  
- Column names  
- Conditions or filters  
- Attribute values  

Entity annotations allow the chatbot to extract structured information from user queries and convert them into appropriate database operations.

### Lookup Tables
Lookup tables are included to enhance entity recognition performance. These tables contain predefined lists of domain-specific vocabulary, such as database schema elements and SQL-related terminology.

Lookup tables improve the model’s ability to recognize entities that may appear in multiple linguistic forms.

## Data Format
The dataset follows the **Rasa YAML format**, which organizes training data into structured sections including:

- `nlu` – Natural language training data  
- `intent` – User intent definitions  
- `examples` – Annotated example utterances  
- `lookup` – Domain-specific vocabulary lists  

This structure ensures compatibility with the **Rasa NLU training pipeline**.

## Dataset Purpose
The dataset enables the chatbot to:

- Accurately classify user intents  
- Extract relevant entities from natural language queries  
- Interpret SQL-related requests expressed in conversational language  
- Support interactive learning of SQL concepts

## Reproducibility
The dataset is publicly provided to support **reproducibility of the experimental results reported in the associated research study**. Researchers and developers may use this dataset to replicate the training process, evaluate NLU performance, or extend the chatbot with additional intents and entities.

## Limitations
Although the dataset includes diverse phrasing variations, it is primarily focused on **SQL learning interactions within a controlled domain**. Future work may extend the dataset by incorporating additional query types, expanded vocabulary, and multilingual training examples.
