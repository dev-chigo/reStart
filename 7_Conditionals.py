"""
A section of code that compares two pieces of information is called a conditional 
statement. You can use conditionals to create different paths through the program. 
Using comparative operators, you will write a program that makes decisions.
"""
#Use the input() function to get information from the user:

#userReply = input("Do you need to ship a package? (Enter yes or no)")
#if userReply == "yes":
  #  print("We can help you ship that package!")
    #Note: The == symbol is a comparative operator. It means is equal to.
#else:
     #   print("Please come back when you need to ship a package. Thank you.")
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy)") 
#serviceType = "envelope" or "Copy"
StampReply = input("What type of stamp would you like? (Enter Good, Bad)")
StampsType = "Good" or "Bad"        
if userReply == "stamps" or "Stamps" or "stamp" or "Stamp":
    print("We have many stamp designs to choose from.")
    if StampsType == "Good":
        print("Good Stamp Selected")
    elif StampsType == "Bad":
        print("Bad Stamps")
    else: 
        print("These are all we have!")
elif userReply == "envelope":
    print("We have many envelopes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a numer) ")
    print("Here are {} copies copies.".format(copies))
else:
    print("Thank you, please again")