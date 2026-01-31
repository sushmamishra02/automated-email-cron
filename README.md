Automated Email Notification System (Python + Linux + Cron)

Overview
This project implements an automated email notification system using Python and the Linux sendmail utility, scheduled with cron. It reads a CSV of participants, personalizes each message, and sends mail respectively. This design fits locked-down enterprise environments where SMTP credentials or cloud APIs cannot be used.

Features
- No SMTP credentials or cloud APIs required; uses system mail (sendmail)
- Personalizes message per participant
- Simple CSV-driven workflow
- Cron-friendly with absolute paths and file-based logging

High-Level Architecture
Cron Scheduler
 → Python Script (auto_mail.py)
 → CSV File (participant data)
 → Linux sendmail
 → Email Recipients

Repository Structure
Recommended layout:
- auto_mail.py               # Main Python script (executable)
- new_participants.csv       # Input CSV (see schema below)
- README.md                  # This documentation
- logs/                      # Runtime logs (not committed)


Prerequisites
- Linux server with sendmail available (typically provided by postfix/sendmail packages)
  - Verify with: which sendmail (often /usr/sbin/sendmail)
- Python 3.8+
- pandas Python library for CSV processing

Install Python dependency (if needed)
pip install --user pandas

CSV File Format
Place or generate a CSV with the following headers:

name,email,summary

User One,user1@example.com, Do not forget to share your DAILY STATUS REPORT!!!!...

Column descriptions
- name: Used to personalize email
- email: Recipient email address
- summary: Email message content

How It Works
1) Script reads the CSV records.
2) For each participant, constructs a basic email with proper headers (From, To, Subject) and personalized body using the summary column.
3) Invokes system sendmail via subprocess to deliver the message.

Running the Script Manually
Using Python directly
python3 /auto_mail.py

Or using executable mode
chmod +x /auto_mail.py
./auto_mail.py

Note: The script should start with a shebang so it can be executed directly:
#!/usr/bin/env python3

Cron Scheduling
Goal: Run at 5:00 PM, Monday to Friday.

Crontab entry
0 17 * * 1-5 /scratch/user/code/auto_mail.py >> /scratch/user/logs/auto_mail.log 2>&1

Steps
1) Ensure the script is executable and uses absolute paths.
2) Create the logs directory and set write permissions for the cron user:
   mkdir -p /scratch/user/logs
3) Edit the cron for the desired user:
   crontab -e
4) Paste the cron line shown above and save.


Logging
- All output and errors are redirected to: /scratch/user/logs/auto_mail.log

Security & Enterprise Considerations
- No SMTP usernames/passwords stored
- No cloud API keys used
- Relies on system-configured MTA (sendmail)
- Suitable for restricted corporate environments
- If required, mask or exclude sensitive CSV data before committing to Git

