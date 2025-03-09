import requests

# Replace with your LeetCode username
username = input("Type the Username as per the LeetCode\n")
url = f"https://leetcode-stats-api.herokuapp.com/{username}"

# Fetch data from the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Print the formatted output
    print("📊 LeetCode Stats for:", username)
    print("=" * 30)
    print(f"Total Solved: {data.get('totalSolved')} / {data.get('totalQuestions')}")
    print(f"Easy: {data.get('easySolved')} / {data.get('totalEasy')}")
    print(f"Medium: {data.get('mediumSolved')} / {data.get('totalMedium')}")
    print(f"Hard: {data.get('hardSolved')} / {data.get('totalHard')}")
    print(f"Acceptance Rate: {data.get('acceptanceRate')}%")
    print(f"Global Ranking: {data.get('ranking')}")
    print(f"Contribution Points: {data.get('contributionPoints')}")
else:
    print("❌ Failed to fetch data. Check the username or API status.")
