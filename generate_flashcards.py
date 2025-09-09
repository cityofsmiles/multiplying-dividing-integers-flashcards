import sympy as sp
import random
import json
import os


flashcards = []


def format_int(n: int) -> str:
    """Format integer for display, enclosing negatives in parentheses."""
    return f"({n})" if n < 0 else str(n)


def generate_case(case_type: int) -> dict:
    """
    Generate a flashcard for one of four cases:
      1. Multiplying like signs
      2. Multiplying unlike signs
      3. Dividing like signs
      4. Dividing unlike signs
    """

    if case_type == 1:  # Multiplying like signs → product positive
        sign = random.choice([1, -1])
        a = random.randint(1, 15) * sign
        b = random.randint(1, 15) * sign
        question = f"{format_int(a)} × {format_int(b)}"
        answer = a * b

    elif case_type == 2:  # Multiplying unlike signs → product negative
        a = random.randint(1, 15)
        b = -random.randint(1, 15)
        if random.choice([True, False]):
            a, b = b, a
        question = f"{format_int(a)} × {format_int(b)}"
        answer = a * b

    elif case_type == 3:  # Dividing like signs → quotient positive
        sign = random.choice([1, -1])
        divisor = random.randint(1, 15) * sign
        quotient = random.randint(1, 15)
        dividend = divisor * quotient
        question = f"{format_int(dividend)} ÷ {format_int(divisor)}"
        answer = quotient

    else:  # case_type == 4 → Dividing unlike signs → quotient negative
        divisor = random.randint(1, 15)
        quotient = random.randint(1, 15)
        dividend = divisor * quotient
        # Flip sign of one of them
        if random.choice([True, False]):
            dividend = -dividend
        else:
            divisor = -divisor
        question = f"{format_int(dividend)} ÷ {format_int(divisor)}"
        answer = dividend // divisor  # guaranteed integer

    return {"question": question, "answer": str(answer)}


# Generate 200 flashcards (50 per case)
for case_type in range(1, 5):
    for _ in range(50):
        flashcards.append(generate_case(case_type))

# Save to ./public/flashcards.json
output_dir = os.path.join(os.getcwd(), "public")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "flashcards.json")

with open(output_path, "w") as f:
    json.dump(flashcards, f, indent=2)

print(f"✅ flashcards.json generated with {len(flashcards)} flashcards at {output_path}")