import json
from pprint import pprint
import sys

try:
  with open(sys.argv[1]) as json_data:
    data = json.load(json_data)
except FileNotFoundError:
  print("The first argument should be the name of the JSON file.")
  exit()

members = data['members'].values()
registered_paid = [x for x in members if len(x['square_receipt']) > 0]
registered_unpaid = [x for x in members if len(x['square_receipt']) == 0]

if len(sys.argv) > 2:
  if sys.argv[2] == "unpaid_emails":
    emails = [x['email'] for x in registered_unpaid]
    print(emails)
  elif sys.argv[2] == "all_emails":
    emails = [x['email'] for x in members]
    print(emails)
  elif sys.argv[2] == "paid_names":
    names = [x['first_name'] + " " + x['last_name'] for x in registered_paid]
    print(names)
  else:
    print("Try one of unpaid_emails, all_emails or paid_names")
else:
  print("You must give a command. Try unpaid_emails, all_emails or paid_names")