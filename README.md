# Password-authentication
This is a Python function that prompts the user to enter a password and checks if it meets certain requirements.

The password must be at least 10 characters long and must match the string "parolaparola". 
If the user enters a password that is too short (less than 4 characters), the function informs the user that their password is too short and decrements
the "tries" counter by 1. If the user enters a password that is between 4 and 10 characters long, the function informs the user that their password is too short
and decrements the "tries" counter by 1. If the user enters a password that is not "parolaparola" and is longer than 10 characters, the function informs the user
that their password is wrong and decrements the "tries" counter by 1.

If the user enters the correct password ("parolaparola"), the function prints "You're logged in!" and returns True, indicating that the login was successful. 
If the user runs out of tries (the "tries" counter reaches 0), the function prints "Try again tomorrow".

Overall, this function is an example of password authentication logic in Python.
