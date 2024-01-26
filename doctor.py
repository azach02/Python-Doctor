import random

hedges = [
    "Please elaborate.",
    "I'd like to hear more.",
    "Could you provide additional details?",
    "It's interesting, tell me more.",
    "I'm intrigued, go on.",
    "I appreciate your input. Can you expand on that?"
]

qualifiers = [
    "Why do you believe that ",
    "It seems you think that ",
    "Can you explain why ",
    "I'm curious about your perspective on ",
    "What leads you to the conclusion that ",
    "In what way do you think that "
]

replacements = {
    "I": "you",
    "me": "you",
    "my": "your",
    "we": "you",
    "us": "you",
    "am": "are",
    "mine": "yours",
    "myself": "yourself",
    "our": "your",
    "ours": "yours",
    "I'd": "you would"
}

def reply(sentence):
    """Builds and returns a reply to the sentence."""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + change_person(sentence)

def change_person(sentence):
    """Replaces first person pronouns with second person pronouns."""
    words = sentence.split()
    reply_words = [replacements.get(word, word) for word in words]
    return " ".join(reply_words)

def main():
    """Handles the interaction between the user and the simulated doctor."""
    print("Good morning! How are you feeling today?")
    print("What can I do for you?")
    
    while True:
        sentence = input("\n»› ")
        if sentence.upper() == "QUIT":
            print("Have a great day!")
            break
        print(reply(sentence))

# The entry point for program execution
if __name__ == "__main__":
    main()
