#Database System
#Callum Grierson
#Input a database of personal information, view that information and quit.
#Development 20/06/2024 - 

#Creating the user database file
a = open("userdata.txt", 'a+')
#Importing time for sleep function - to let text file update before returning to menu
import time
#Creating the Input system and variables

def inputSystem():
    print ("Please input your Details Below")
    maxLengthInput = 2
    inputList = []    
    #Setting List size for our parameters and allowing changes for that size
    while len(inputList) < maxLengthInput:
    #Asking for each bit of information and putting them into the list
        savedInput = input("Enter your Username: ")
        inputList.append(savedInput)
        print(inputList)
        savedInput = input("Enter your Password: ")
        inputList.append(savedInput)
        print(inputList)
        savedInput = input("Enter your URL/Resource: ")
        inputList.append(savedInput)
        print(inputList)
        listNumber = 0
        #Making sure that the information is correct and if not it deletes the list and starts over
        print ("Is this correct?")
        print (inputList)
        print ("If not then please type 'No', if Correct type 'Yes': ")
        promptUser = input("")
        if promptUser == "No":  
            print ("Please Enter Again") 
            inputList = []
            inputSystem()
    #If the list is correct it writes it to a text document in approriate style
        elif promptUser == "Yes":  
            a = open("userdata.txt", 'a+')
            a.write("Entry " + str(listNumber) + str(inputList) + "\n")
            listNumber + 1
            print(a.read())
            print("Please wait while we update our database")
            time.sleep(10)
            #After entry it reroutes back to Menu
            Menu()
        else: print("I couldn't understand, returning to menu") , Menu()
          
#Creating the View system for the file
def viewSystem():
            #Opening the file in read only, allowing for access back to the menu
            a = open("userdata.txt", 'r')
            print(a.read())
            time.sleep(2)
            print("To return to menu please type Menu")
            promptUser = input("")
            if promptUser == "Menu":
                Menu()
            else: print("Sorry I didn't understand, Try again"), time.sleep(2) ,viewSystem()


#Creating the Menu
def Menu():
    print ("Welcome to the Database System, Please Type The first word of your desired action: \n", "Add Credentials\n", "View Credentials\n", "Exit")
    #Prompts the user for an input
    promptUser = input("")
    if promptUser == "Add":
        #Takes you to the input system
        inputSystem()
    elif promptUser == "View":
        #Takes you to view the database - sleep is to let it update any recent additions
        time.sleep(5)
        viewSystem()
    elif promptUser == "Exit":
         #Stops the script
         exit()
    else: print ("Sorry please try again") , Menu()


#Intialisation of Script
Menu()
