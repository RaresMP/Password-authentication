#the old code
def password():
    # Set the number of tries to 3
    tries = 3
    
    # Loop while the user has tries remaining
    while tries > 0:
        # Prompt the user to enter a password
        parola = input("Enter a password: ")
        
        # Check if the password is too short (less than 4 characters)
        if len(parola) < 4:
            print("You're password is too short!Try again!")
            
            # Decrement the tries counter
            tries -= 1
            
            # Inform the user how many tries they have left
            print("You have " + str(tries) + " tries.")
        
        # Check if the password is between 4 and 10 characters long
        elif 4 < len(parola) < 10:
            print("You're password is too short!Try again!")
            
            # Decrement the tries counter
            tries -= 1
            
            # Inform the user how many tries they have left
            print("You have " + str(tries) + " tries.")
        
        # Check if the password is correct
        elif len(parola) >= 10 and parola == "parolaparola":
            print("You're logged in!")
            
            # Return True to indicate the user has been logged in
            return True
        
        # If the password is neither too short nor correct, inform the user it's wrong
        else:
            print("Wrong password")
            
            # Decrement the tries counter
            tries -= 1
            
            # Inform the user how many tries they have left
            print("You have " + str(tries) + " tries.")
    
    # If the user has run out of tries, inform them they can't try again until tomorrow
    print("Try again tomorrow")



password()




# the new code
def password():
    # Set the number of tries to 3
    tries = 3
    
    # Loop while the user has tries remaining
    while tries > 0:
        # Prompt the user to enter a password
        password = input("Enter a password: ")
        
        # Check if the password is too short
        if len(password) < 10:
            print("Your password is too short! Try again.")
        
        # Check if the password is correct
        elif password == "parolaparola":
            print("You're logged in!")
            return True
        
        # If the password is neither too short nor correct, inform the user it's wrong
        else:
            print("Wrong password. Try again.")
        
        # Decrement the tries counter
        tries -= 1
        
        # If the user has tries remaining, inform them how many tries they have left
        if tries > 0:
            print(f"You have {tries} tries left.")
    
    # If the user has run out of tries, inform them they can't try again until tomorrow
    print("Sorry, you've run out of tries. Try again tomorrow.")
