"""
Your test questions.
"""

QUESTIONS = [
    {
        "question": "Is a bike worth it for a 20-minute walking commute?",
        "expects": "storage",
    },
    {
        "question": "How much does covered bike parking cost, and is it easy to find?",
        "expects": "full by 9am",
    },
    {
        "question": "Who should I talk to about changing my major in second year?",
        "expects": "department adviser for the major you want",
    },
    {
        "question": "How many clubs should a first-year student join?",
        "expects": "two",
    },
    {
        "question": "What do commuting students say about locker rentals?",
        "expects": "$20 a year",
    },
]


OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]

def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
