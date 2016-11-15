from twilio.rest import TwilioRestClient as Client

account_sid = "ACfe127e3dc924a8f03e4408b8df362213" # Your Account SID from www.twilio.com/console
auth_token  = "7eb22879e85c9e15794d9db5d82e3713"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

message = client.messages.create(to="+14127597759", from_="+14127278169", body="Hello from Xue's Python Code!")

print(message.sid)



#if name == '__main__':
