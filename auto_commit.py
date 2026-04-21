import os
import random
from datetime import datetime

# Randomly determine the number of submissions for today (0 to 5 times)
commit_count = random.randint(0, 5)

def make_commit():
    # Append content to data.txt and cause file changes
    with open("data.txt", "a") as f:
        f.write(f"Update: {datetime.now().isoformat()} - Random ID: {random.random()}\n")
    
    # Execute Git commands
    os.system('git add data.txt')
    os.system(f'git commit -m "chore: auto update {datetime.now().strftime("%Y-%m-%d")}"')

if __name__ == "__main__":
    if commit_count > 0:
        for _ in range(commit_count):
            make_commit()
        print(f"success:Today commited {commit_count} times.")
    else:
        print("Today is holiday, no commit.")