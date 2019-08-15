import re

def valid_email(email):
    pattern = re.compile(r'^[\w.-]+@[\w]+\.[a-z]{1,3}\b\.{,1}[a-z]{,2}$')
    match = pattern.search(email)
    return match

def filter_email(emails):
    allowed_emails = list(filter(valid_email, emails))
    return allowed_emails
