import random
import time
sentences = [
    "Python is a powerful programming language.",
    "Coding is fun and challenging.",
    "I love building projects with code."
]
target_text = random.choice(sentences)
print("Type the following sentence exactly as shown:")
print(target_text)
quastion = input("Press Enter when you are ready...")
start_time = time.time()
user_input = input("\n Type here:")
end_time = time.time()
time_taken = end_time - start_time
if user_input == target_text:
    print("Accuracy: 100%")
else:
    print("Accuracy: 0% (You made a mistake)")
total_words = len(target_text.split())
minutes = time_taken / 60
wpm = total_words / minutes
print("\n--- RESULTS ---")
print(f"Time taken: {round(time_taken, 2)} seconds")
print(f"Speed: {round(wpm, 2)} Words Per Minute (WPM)")
print("-" * 40)