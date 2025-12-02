from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")
call_sid    = os.getenv("CALL_SID")

client = Client(account_sid, auth_token)

# Fetch call info
call = client.calls(call_sid).fetch()

print("From:", call.from_)
print("To:", call.to)
print("Status:", call.status)
print("Start Time:", call.start_time)
print("End Time:", call.end_time)
print("Duration (seconds):", call.duration)
