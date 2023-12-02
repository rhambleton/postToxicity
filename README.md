# Post Toxicity Checker
### A simple tool to screen social media posts before they are posted online.

## How It works
- A simple web interface allows the user to enter a message.
- The message text is screened by an AI model before the it is posted on the social media website.
- If the post appears toxic, an alert is displayed the user is given two options
    - Continue - the message will be posted online, and a copy will be emailed to the users parent.
    - Cancel - the user is given the chance to reword their message before posting.
  
## System Components
- A simple web interface (website/default.html)
- A python API that passes the message through a pretrained AI model (main.py)