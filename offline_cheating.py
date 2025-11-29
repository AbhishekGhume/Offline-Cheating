import time
import keyboard
import pyperclip
from transformers import AutoTokenizer, AutoModelForCausalLM

# Choose your model – here we use a sample code-generation model.
# Make sure to download and cache the model locally.
model_name = "Salesforce/codegen-350M-mono"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_code(problem_statement):
    # Encode the input problem statement.
    input_ids = tokenizer.encode(problem_statement, return_tensors="pt")
    
    # Generate code with a chosen max length and sampling parameters.
    output_ids = model.generate(input_ids, 
                                max_length=512, 
                                do_sample=True, 
                                temperature=0.7,
                                top_p=0.95)
    
    # Decode the generated tokens to text.
    generated_code = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return generated_code

def wait_for_clipboard_change(initial_text, timeout=30):
    """Wait for the clipboard content to change (up to timeout seconds)."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        current_text = pyperclip.paste()
        if current_text != initial_text:
            return current_text
        time.sleep(0.5)
    return None

def on_activate():
    print("[Activated] Waiting for a new problem statement in your clipboard...")
    # Save current clipboard content.
    initial_clipboard = pyperclip.paste()
    
    # Wait for clipboard to change.
    problem_statement = wait_for_clipboard_change(initial_clipboard)
    if problem_statement:
        print("Problem statement detected. Generating Java code...")
        generated_code = generate_code(problem_statement)
        pyperclip.copy(generated_code)
        print("Generated code has been copied to the clipboard!")
    else:
        print("No new clipboard content detected. Try copying a problem statement again.")

def main():
    print("=== Local Code Generation Tool ===")
    print("Press 'Ctrl+Alt+A' to activate and generate code from a copied problem statement.")
    print("Press 'Ctrl+Alt+D' to deactivate and exit the tool.")
    
    # Bind activation hotkey.
    keyboard.add_hotkey("ctrl+alt+a", on_activate)
    
    # Wait for deactivation hotkey.
    keyboard.wait("ctrl+alt+d")
    print("Tool deactivated. Exiting...")

if __name__ == '__main__':
    main()