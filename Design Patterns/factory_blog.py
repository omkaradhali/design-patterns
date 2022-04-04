
from dataclasses import dataclass


@dataclass()
class User:
  first_name: str
  last_name: str
  email_address: str
  phone_number: str
  

class EmailNotification():
  def __init__(self, user):
    self.user = user
  
  def send_notification(self):
    print(f"Email Notification sent to {self.user.first_name} {self.user.last_name} at {self.user.email_address}")

class SMSNotification():
  def __init__(self, user):
    self.user = user
    
  def send_sms_notification(self):
    print(f"SMS Notification sent to {self.user.first_name} {self.user.last_name} at {self.user.phone_number}")
 
if __name__ == "__main__":
  user = User("John", "Doe","john_doe@gmail.com", "1234567899")
  email_notification = EmailNotification(user)
  sms_notification = SMSNotification(user)
  email_notification.send_notification()
  sms_notification.send_sms_notification()