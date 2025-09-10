import os

SUBMISSIONS_DIR = "submissions"
LEADERBOARD_FILE = "leaderboard.md"

def score_submission(username):
    score = 0
    user_dir = os.path.join(SUBMISSIONS_DIR, username)
    project_file = os.path.join(user_dir, "project.md")

    if os.path.exists(project_file):
        score += 1  # Valid submission

        with open(project_file, "r") as f:
            content = f.read()
            if "## Documentation" in content:
                score += 2
            if "## Tests" in content:
                score += 3
            if "## Creativity" in content:
                score += 4

    return score

def update_leaderboard():
    users = [d for d in os.listdir(SUBMISSIONS_DIR) if os.path.isdir(os.path.join(SUBMISSIONS_DIR, d))]
    scores = [(user, score_submission(user)) for user in users]
    scores.sort(key=lambda x: x[1], reverse=True)

    with open(LEADERBOARD_FILE, "w") as f:
        f.write("# 🏆 Hackathon Leaderboard\n\n")
        f.write("| Rank | Username | Score |\n")
        f.write("|------|----------|-------|\n")
        for i, (user, score) in enumerate(scores, start=1):
            f.write(f"| {i} | {user} | {score} |\n")

if __name__ == "__main__":
    update_leaderboard()
