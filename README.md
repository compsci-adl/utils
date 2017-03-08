# utils

```bash
python3 process_members.py <json_file> <command>
```

Takes an export of the Firebase database, and performs a number of commands.

- `unpaid_emails`: Produces a list of emails for students who've registered online but not yet paid.
- `paid_names`: Produces the names of all students who've registered, and paid their membership fee.
- `all_emails`: Produces a list of emails for all students who've registered.

If you run with `python3`, the emails won't have the unicode `'u'` attached, and you can copy them straight into your email client.