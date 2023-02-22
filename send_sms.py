from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

#this is the main text where the message will be shown 
#below an string join in an array added with a range of 10
my_msg = ''.join(['bigman ting yeah\n' for i in range(10)])

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)
