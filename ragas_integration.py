import json
import os
import random

# Input/Output paths
INPUT_FILE = "data/sample_log.json"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ragas_scores.json")

def load_data():
    """Load input log JSON"""
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def mock_ragas_scores(log_data):
    """
    Generate realistic mock RAGAS scores for faithfulness, answer_relevancy, and context_precision.
    Values are randomly chosen within a reasonable range to simulate actual evaluation results.
    """
    output_data = []
    for item in log_data:
        output_data.append({
            "id": item["id"],
            "faithfulness": round(random.uniform(0.75, 0.95), 2),
            "answer_relevancy": round(random.uniform(0.70, 0.90), 2),
            "context_precision": round(random.uniform(0.80, 0.95), 2)
        })
    return output_data

def main():
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Loading log data...")
    log_data = load_data()

    print("Simulating RAGAS evaluation (mock mode)...")
    output_data = mock_ragas_scores(log_data)

    # Save mock results
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print(f"Mock results saved at {OUTPUT_FILE}")
    print("NOTE: This is a mock mode. Replace it with real LLM evaluation for production.")

if __name__ == "__main__":
    main()
