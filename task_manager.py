#This program helps a small business managed tasks assigned to each member 

#=====importing libraries===========
#Information from the text file is open and read 
user =open('user.txt', 'r')
task = open('tasks.txt', 'r')

#this is to read every line in the text files and are stored in the variables
line = user.readlines()
activities = task.readlines()

#These two variables are used to store the usernames and password to allow the program to read them seperately when a user logs in
#They are used to compare the information  provided by the user. If the information matches the user gains access to the menu options
user =[]
password =[]

#For loop to seperate the usernames and passwords from the user.txt file
for i in range(len(line)):
    position = line[i].strip()
    position = position.split(", ")
    user.append(position[0])
    password.append(position[1])

#====Login Section====

#User inputs their username and password to login 
user_name = str(input('Enter your username: '))

#While loop to verify if the username provided by the user exists. If the username exists, it will allow the user to provide their password and also verify  it
while user_name not in user :
    user_name = str(input('Username does not exist! Try again: '))
else:
     #this identifies the index or position of the username in the user.txt file and extracts the corresponding password based on that position
     userposition = line[user.index(user_name)].strip()
     userposition = userposition.split(", ")
     password = userposition[1]

     user_password = str(input('Enter your password: '))

     #if passwords do not match the user will be prompted to enter the password again until the correct one is entered
     while user_password != password:
         user_password = str(input('Incorrect password! Try again: '))

print('\n')

#This while loop is executed if the user logs in successfully.
while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
s - To view statistics
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

#if statement to allow the user to register a new user
#it only allows the admin user to register new users
 
    if menu == 'r':
        pass
        if user_name == 'admin':
            new_user = str(input('Enter new username: '))
            
            #If the entered username already exists, a different username will be requested
            while new_user in user:
                new_user = str(input('User already exists! Please enter a different username: '))

            #User is prompted to enter a new password if the username was accepted by the program
            new_password = input('Enter new password: ')
            password_confirm = input('Confirm new password: ')

            #while loop to confirm if the passwords entered match together
            while password_confirm != new_password:
                password_confirm = input('Passwords do not match!!! Confirm again: ')
            else:
                user = open('user.txt', 'a+')
                user.write(f'\n{new_user}, {password_confirm}')
                print('User added successfully!')
                user.close()
                
        else: 
            print('\n')
            print('Your are not authorised to register new users!')    
            
    #This statement only allows the admin user to view statistics about the users and tasks
    elif menu == 's':
        if user_name == 'admin':
            print(f'Total number of tasks: {len(activities)}\nTotal number of users: {len(line)} ')
        else:
            print('\n')
            print('You are not authorised to view this menu option!')

    #This allows a task to be assigned to a user
    elif menu == 'a':
        pass
        task_user = input('Enter username of the person whom the task is assigned to: ')

        #while loop to verify if the user entered exists or not.
        while task_user not in user:
            
            task_user = str(input('User does not exist! Please enter a correct username: '))

        #User is prompted to enter details about the task
        task_title = input('Enter the title of the task: ')
        task_description = input('Enter the description of the task: ')
        due_date = input('Enter the due date of the task (e.g 03 March 2023): ')
        current_date = input('Enter the current date (e.g 03 March 2023): ')
    
        task_complete = input('Is the task complete? (yes/no): ').lower()

        #a while loop  that prints an appropriate message  depending on the user input. It accepts  a yes or no as valid input from the user.
        while  task_complete != 'yes' and task_complete != 'no':
            print("Invalid input")
            task_complete = str(input('Is the task complete? (yes/no): ')).lower()
        else:
           if  task_complete == 'yes':
               completion = 'Yes'
           elif task_complete == 'no':
               completion ='No'

        #the details about the task are added to the tasks.txt file
        task = open('tasks.txt', 'a+')
        task.write(f'\n{task_user}, {task_title}, {task_description}, {due_date}, {current_date}, {completion}')
        task.close()
    
    #this allows the user to view all the tasks
    elif menu == 'va':
        pass
        lines = open('tasks.txt', 'r+')
        usertasks = lines.readlines()

        #loop to allows the tasks to be printed in user_friendly manner
        for x in range(len(usertasks)):
            sentence = usertasks[x].split(', ')
            sentence1 = f"\nTask: {sentence[1]}\nAssigned to: {sentence[0]}\nDate assigned: {sentence[4]}\nDue Date: {sentence[3]}\nTask complete?: {sentence[5]}\nTask description: {sentence[2]} "
            
            print(sentence1)
            lines.close()
    #this allows the current user that is logged in to view their task.
    elif menu == 'vm':
        pass

        lines = open('tasks.txt', 'r+')
        usertasks = lines.readlines()
        
        
        #user names are extracted in the tasks.txt file and stored in the names variable
        names = []
        for u in range(len(usertasks)):
            task = usertasks[u].split(', ')
            names.append(task[0])
        
        #The tasks information is extracted based on the on the index of the username in the tasks.txt file
        if user_name in names:
           output = usertasks[names.index(user_name)].split(', ')
           output_final = f"\nTask: {output[1]}\nAssigned to: {output[0]}\nDate assigned: {output[4]}\nDue Date: {output[3]}\nTask complete?: {output[5]}\nTask description: {output[2]}\n "
           print(output_final)
           lines.close()


    #Allows the user to exit the program
    elif menu == 'e':
        print('Goodbye!!!')
        
        exit()
    else:
        print("You have made a wrong choice, Please Try again")




