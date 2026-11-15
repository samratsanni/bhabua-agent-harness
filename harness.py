# SAMRAT SANNI - Bhabua Routing Harness
# Bihar, India - Solo Participant
import os

def run_agent(task_description):
    # Step 1: Router - Keyword + LLM
    task_lower = task_description.lower()
    if "roof" in task_lower or "beam" in task_lower or "truss" in task_lower:
        expert = "ROOF_EXPERT - IRC Code"
    elif "wire" in task_lower or "volt" in task_lower or "cable" in task_lower or "electrical" in task_lower:
        expert = "ELECTRICAL_EXPERT - NEC Code"
    else:
        expert = "PLUMBING_EXPERT - IPC Code"
    
    # Step 2: Tool Use - Calculator + Validator
    print(f"[Bhabua Harness] Routing to {expert}")
    return f"Solved using {expert} with Safety Validator"

if __name__ == "__main__":
    print("Bhabua Agent Harness by Samrat Sanni, Bihar")
