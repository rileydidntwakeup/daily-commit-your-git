# Daily Commit Your Git

Daily Commit Your Git provides a human-like automation tool to maintain your GitHub contribution grid. By generating a random number of commits, it creates a natural variation in the green wall's intensity. Furthermore, it significantly reduces activity on weekends to better simulate a healthy work-life balance.

## Installation

1.  **Fork** this repository.
2.  **Enable Actions**: Go to the `Actions` tab of your forked repo and click **"Enable"**.
3.  **Permissions**:
    * Navigate to `Settings` > `Actions` > `General`.
    * Scroll to **Workflow permissions**.
    * Select **"Read and write permissions"** and hit **Save**. 💾
4.  **First Run**: Go back to `Actions`, select **Daily Auto Commit**, and click **Run workflow** to see your first green brick! 🧱

##  Customization

You can tweak the "vibe" of your commits in `auto_commit.py`:

```python
# Change the numbers to fit your style!
if weekday < 5:
    commit_count = random.randint(0, 5) # Weekday range
else:
    # Weekend logic
    if random.random() < 0.75:
        commit_count = 0 # Most weekends off
```

##  Project Structure

* `.github/workflows/daily_commit.yml`: The "alarm clock" that triggers the script.
* `auto_commit.py`: The brain that handles the logic and Git commands.
* `data.txt`: The log file where the automated changes are recorded.

##  License

Distributed under the **MIT License**. Use it for fun, learning, and aesthetic purposes! 

---

### 💡 Pro Tip
To see your private contributions on your profile, make sure to go to your **Contribution Settings** (above the green wall on your profile) and check **"Private contributions"**.

Happy coding! 💻✨ 
