from jira import JIRA

jira_server = {'server': 'https://dilshandilip.atlassian.net'}
jira_token = ""
email = ''

jira = JIRA(jira_server, basic_auth=(email, jira_token))
projects = jira.projects()
# print(projects)

with open("jira_ticket.txt", "r") as file:
    issue_keys = file.readlines()
    # print(issue_keys)

issue_keys = [line.strip() for line in issue_keys]

for issue_key in issue_keys:
    try:
        print(issue_key)
        issue = jira.issue(issue_key)
        issue.delete()
        print(issue)
    except Exception as e:
        print(e)


# delete all tickets in jira project
# for project in projects:
#     jql_str = f"project={project}"
#     issues = jira.search_issues(jql_str)
#     for issue in issues:
#         print(issue)
#         issue.delete()