import colorama
import random
from colorama import Fore, Style

colorama.init(autoreset=True)

# Read content from s1.txt and s2.txt
with open("s1.txt", "r") as f:
    story1 = f.read()

with open("s2.txt", "r") as f:
    story2 = f.read()

with open("s3.txt", "r") as f:
    story3 = f.read()

# Randomly choose one of the stories
chosen_story = random.choice([story1, story2, story3])

# Find all placeholders in the chosen story
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(chosen_story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = chosen_story[start_of_word:i + 1]
        words.add(word)

# Prompt user for words and store answers
answers = {}
print(Fore.CYAN + Style.BRIGHT + "Welcome to the world of Mad Libs! Caution: Uncontrollable laughter ahead! 🤣\n")

for word in words:
    ans = input(f"Enter a word for {word}: ")
    answers[word] = ans

print()

# Generate and print the final story with filled-in words
print(Fore.MAGENTA + Style.BRIGHT + "Mad Libs Story:")
print()

final_story = chosen_story
for word, answer in answers.items():
    final_story = final_story.replace(word, answer)

print(final_story)
