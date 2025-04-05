
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_model():
    model_id = "Salesforce/codegen-350M-mono"  # Lightweight model
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)
