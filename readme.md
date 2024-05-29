# Jira Ticket Deletion Tool

This Python script automates the process of deleting tickets from a Jira project. It utilizes the Jira API provided by the `jira` library to interact with a Jira instance and perform ticket deletion based on specified criteria.

## Requirements

- Python 3.x
- `jira` library

## Setup

1. **Install Required Packages**: Make sure you have the `jira` library installed. You can install it via pip:

   ```
   pip install jira
   ```

2. **Configure Jira Connection**: Provide the necessary information to connect to your Jira instance:

   - `jira_server`: The URL of your Jira server.
   - `jira_token`: Your Jira API token or password.
   - `email`: Your email address associated with your Jira account.

3. **Run the Script**: Execute the script in your Python environment.

## Usage

1. **Delete Tickets**: Uncomment the section in the script responsible for deleting tickets. By default, the script is configured to read ticket keys from a file named `jira_ticket.txt` and delete the corresponding tickets from Jira.

2. **Execute Script**: After setting up the script, run it in your Python environment. It will delete the tickets specified by the criteria.

## Additional Notes

- Ensure that the user account associated with the provided email address has sufficient permissions to delete tickets in the specified projects.
- Exercise caution when deleting tickets, as this action is irreversible.
- Regularly review and update the script to accommodate changes in your Jira instance or requirements.