# At first we will import requests module for python to communicate with websites or API's(here communication towards Github repo's)
import requests

# Using GitHub RESTAPI Doc we can fetch pull request URL, then making a GET request to fetch pull requests data from the GitHub API and storing the response in a variable
response = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')

# checking if the response is successful
if response.status_code == 200:
  
    # Converting the JSON response to a dictionary for accessing its key-value pairs
    pull_requests = response.json()

    # Creating an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterating through each pull request and extracting the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1           #modifying count values
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():       # to retrive both keys and values we use .items, otherwise "for"/"if" only checks the keys not values
        print(f"{creator}: {count} Pull Requests")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}") #response.status_code will give the codes like 200=OK, 404=Notfound, 503=service temporarily unavailable

