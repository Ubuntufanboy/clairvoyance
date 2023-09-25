"""
This file is what will be run by the bus driver

Write functions for the following

1. Update location (Which bus stop)
2. Report delay (use "import feed" and "feed.delay(time_in_minutes)")
3. Message parents (Use "import feed" and "feed.messAage(parent, msg) parent should be a class)
4. Report suspisous activity (use "import feed" and "feed.report(msg)")
5. allow parents to sign up
"""

import feed

# This is a blueprint for parents

class Parent:
    def __init__(self, name):
        self.name = name
    
        self.alerts = [] # empty but might get alerts later


def make_parent(name):
    global list_of_parents
    list_of_parents = []
    list_of_parents.append(Parent(name))

def update_location():
    global location
    location = input("What was the most recent bus stop you've passed or currently at? \n ") 

def report_delay(length_of_time):
    feed.delay(length_of_time)

def report_suspicious_activity(reported_message):
    feed.report(reported_message)


choice = input("Type the letter corresponding to the action would you like to make: \n A) Sign Up \n B) Update Location \n C) Report Delay \n D) Report Suspicious Activity \n ")

if choice == "A":
    parent_name = input("What is the parent's first and last name? \n ")
    make_parent(parent_name)

if choice == "B":
    update_location()

if choice == "C":
    delay_length = int(input("How long in minutes is the delay? \n "))
    report_delay(delay_length)

if choice == "D":
    message = input("Write your message here: \n ")
    report_suspicious_activity(message)
    
