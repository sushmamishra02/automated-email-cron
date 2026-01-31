#!/usr/bin/env python3

import pandas as pd
import subprocess

path='/scratch/oraofss/SUSHMA/csv/new_participants.csv'

df= pd.read_csv(path)

for index,row in df.iterrows():
    name=row.get("name")
    email=row.get("email")
    summary=row.get("summary")

    subject='Reminder Mail!'
    body=f"""
    Hi {name},

    {summary}

    Thanks & Regards,
    Well Wisher:)
    """

    email_content=f"""Subject: {subject}
From: Well Wisher <>
To: {email}

{body}
"""
    try:
        subprocess.run(
            ["/usr/sbin/sendmail",email],
            input=email_content,
            universal_newlines=True,
            check=True
        )
        print(f"Successfully sent mail to {email}")
    except Exception as e:
        print(f"Failed to send mail to {email}: {e}")
