# Password-authentication
#How to use:

- Clone or download this repository.
- Open a terminal window in the repository's directory.
- Run the following command to start the program:
python password_checker.py
#How it works:

The program works by first setting the number of tries to 3. Then, it enters a loop that will repeat until either the user enters a valid password or the user runs out of tries.

Within the loop, the program prompts the user to enter a password. The program then checks if the password is too short (less than 10 characters). If the password is not long enough, the program prints a message and decrements the tries counter.

If the password is long enough, the program checks if it matches the string "parolaparola". If it does, the program prints a message and exits the loop. If the password does not match, the program prints a message and decrements the tries counter.

If the tries counter reaches 0, the program prints a message and exits the program.
