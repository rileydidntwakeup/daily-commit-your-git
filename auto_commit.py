import os
import random
from datetime import datetime

# Get current day of the week (0 is Monday, 6 is Sunday)
weekday = datetime.now().weekday()

# --- Human-like logic configuration ---
if weekday < 5:
    # Monday to Friday: 0 to 5 commits
    commit_count = random.randint(0, 5)
    print(f"Today is a weekday (Day {weekday + 1}). Scheduled 0-5 commits.")
else:
    # Weekend Logic: 75% chance of 0 commits, 25% chance of 1-3 commits
    if random.random() < 0.75:
        commit_count = 0
        print(f"Today is the weekend (Day {weekday + 1}). 75% probability hit: Resting.")
    else:
        commit_count = random.randint(1, 3)
        print(f"Today is the weekend (Day {weekday + 1}). 25% probability hit: Minimal work mode.")

def make_commit():
    file_path = "data.txt"
    with open(file_path, "a") as f:
        f.write(f"Log entry: {datetime.now().isoformat()} - Entropy: {random.random()}\n")
    
    os.system('git add data.txt')
    
    messages = [
        "chore: update data logs",
        "docs: fix minor typos in documentation",
        "refactor: improve internal logic",
        "style: format code according to PEP8",
        "fix: resolve minor consistency issues",
        "perf: optimize background processing"
    ]
    selected_msg = random.choice(messages)
    os.system(f'git commit -m "{selected_msg} ({datetime.now().strftime("%Y-%m-%d")})"')

if __name__ == "__main__":
    if commit_count > 0:
        for _ in range(commit_count):
            make_commit()
        print(f"Success: {commit_count} commits generated today.")
    else:
        print("Taking a break. No commits made.")