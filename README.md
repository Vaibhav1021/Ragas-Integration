# Ragas-Integration

## Overview
This project evaluates conversational logs using RAGAS metrics:
- **Faithfulness** – Measures how well the generated answer aligns with the retrieved context.
- **Answer Relevancy** – Evaluates how relevant the generated answer is to the user query.
- **Context Precision** – Checks if the retrieved context is precise and appropriate.

The expected output is a JSON file with the following structure:
```json
[
  {
    "id": "item-001",
    "faithfulness": 0.92,
    "answer_relevancy": 0.88,
    "context_precision": 0.95
  },
  {
    "id": "item-002",
    "faithfulness": 0.84,
    "answer_relevancy": 0.79,
    "context_precision": 0.87
  }
]
```

### Approach

1) Input Data
The script reads input conversational logs from data/sample_log.json.
Each entry contains:

- id – unique identifier
- items.input.system – context
- items.input.user – query
- items.expected_output – expected answer

2) RAGAS Integration
Normally, ragas uses a language model (LLM) like OpenAI GPT to evaluate metrics.
However, to avoid API costs for this demonstration, a mock evaluation mode is implemented, generating realistic placeholder scores for:

- faithfulness
- answer_relevancy
- context_precision

3) Output
Results are saved in output/ragas_scores.json with the correct schema.

4) API-Ready
The code is structured so it can easily switch to real LLM evaluation by integrating OpenAI GPT or any LangChain-supported model with ragas.evaluate().

### Libraries Used
- json – for reading/writing JSON files
- os – for file path handling
- random – to simulate realistic scores

For real evaluation:
- ragas
- langchain-openai

These are not required for the mock version.

### Assumptions and Simplifications
- This version uses mock scores instead of actual LLM API calls to avoid external API billing.
- The mock scores are generated within realistic ranges (0.70–0.95).
- The structure fully matches what would be produced by a real RAGAS evaluation.

### How to Run

1) Clone the repository:
```json
git clone <your-repo-link>.git
cd ragas_assignment
```

2) (Optional) Create a virtual environment:
  ```json
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate.bat   # Windows
```

3) Run the script:
```json
python ragas_integration.py
```

4) Check the output:
 ```json
cat output/ragas_scores.json
```

### Switching to Real Evaluation
 To enable actual LLM evaluation:

1) Install required libraries:
```json
pip install ragas langchain-openai
```

2) Set your OpenAI API key:
```json
export OPENAI_API_KEY="your-key"
```

3) Replace the mock_ragas_scores() call with:
```json

from ragas import evaluate
result = evaluate(dataset, metrics=[faithfulness, answer_relevancy, context_precision], llm=ragas_llm)
```

-----------------------
#### Author  
#### This solution is implemented as part of an internship assignment.  
#### The mock mode was intentionally chosen to demonstrate the approach without incurring API costs.
