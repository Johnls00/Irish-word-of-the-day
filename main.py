import smtplib
from email.message import EmailMessage
import random
import csv

# Define email addresses
FROM_ADDRESS = "Your from email address here"
EMAIL_PASSWORD = "Your sender email password here"
# you can add multiple recieving addresses with a comma
TO_ADDRESS = "Your receiving email address here ,"




# Function to read CSV file
def read_csv(filepath: str):
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                data.append(row)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    return data


# Read data from CSV file
data = read_csv('./data/Irish_words_1-200.csv')

# Randomly choose today's word
todays_word = random.choice(data)

# HTML template for the email with placeholders
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Irish Word of the Day</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333333;
        }}
        .container {{
            width: 100%;
            max-width: 600px;
            margin: 30px auto;
            background-color: #ffffff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            background-color: #007B55;
            color: #ffffff;
            text-align: center;
            padding: 40px 20px;
        }}
        .header h1 {{
            margin: 0;
            font-size: 28px;
            letter-spacing: 1px;
        }}
        .content {{
            padding: 30px 20px;
            text-align: center;
        }}
        .section {{
            margin-bottom: 20px;
        }}
        .section h2 {{
            font-size: 24px;
            color: #007B55;
            margin: 10px 0;
        }}
        .word {{
            font-size: 36px;
            color: #007B55;
            margin-bottom: 10px;
        }}
        .meaning {{
            font-size: 24px;
            color: #333333;
            margin-bottom: 20px;
        }}
        .footer {{
            background-color: #007B55;
            color: #ffffff;
            text-align: center;
            padding: 15px 20px;
            font-size: 14px;
        }}
        .footer a {{
            color: #ffffff;
            text-decoration: none;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Irish Word of the Day</h1>
        </div>
        <div class="content">
            <div class="section">
                <h2>Irish</h2>
                <div class="word">{word}</div>
            </div>
            <div class="section">
                <h2>English</h2>
                <div class="meaning">{meaning}</div>
            </div>
            <div class="section">
                <h2>Pronunciation</h2>
                <a href="https://www.teanglann.ie/en/fuaim/{word}">Listen here</a>
            </div>
        </div>
        <div class="footer">
            © 2024 Irish Word of the Day. All rights reserved.
        </div>
    </div>
</body>
</html>
"""

# Populate the template with dynamic content
#Irish word and english word taken from our daily random word
html_content = html_template.format(
    word=todays_word[0],
    meaning=todays_word[1]
)

# Create the email message
msg = EmailMessage()
msg["Subject"] = "Irish Word Of The Day"
msg["From"] = FROM_ADDRESS
msg["To"] = TO_ADDRESS
msg.set_content("This email requires HTML support to view.")
msg.add_alternative(html_content, subtype='html')

# Send the email
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
