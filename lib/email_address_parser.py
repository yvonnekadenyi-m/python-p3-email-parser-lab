# your code goes here!

# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        #filter_string = re.compile(r'[A-z]\w*\.\w+@\w+\.[a-z]+|[A-z]\w*\@\w+\.[a-z]+')
        #filtered_emails = filter_string.sub("", self.email_addresses)
        #devide = re.compile(r'[,\s]+')
        #emails_list = list(set(devide.split(filtered_emails)))
        #sorted_emails_list = sorted(emails_list, key=lambda v: v[0])
        #return sorted_emails_list

        filter_string = re.compile(r'[A-z]\w*\.\w+@\w+\.[a-z]+|[A-z]\w*\@\w+\.[a-z]+')
        filtered_emails = filter_string.findall(self.email_addresses)
        unique_emails = sorted(set(filtered_emails))
        return unique_emails


        