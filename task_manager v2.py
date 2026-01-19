#This program helps a small business manage tasks assigned to each member 

#Datetime module imported for comapring dates of the tasks
from datetime import datetime

#The reg_user function allows a user to add a new user. Only the admin is authorised to add a new user
def reg_user():
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
                newuser = open('user.txt', 'a+')
                newuser.write(f'\n{new_user}, {password_confirm}')
                print('User added successfully!')       
     else: 
        print('\n')
        print('Your are not authorised to register new users!')    

#============================================================================================================================================

#The add_task function allows a user to add a new task
def add_task():
     task_user = input('Enter username of the person whom the task is assigned to: ')
        #while loop to verify if the user entered exists or not.
     while task_user not in user:
             task_user = str(input('User does not exist! Please enter a correct username: '))

     #User is prompted to enter details about the task
     task_title = input('Enter the title of the task: ')
     task_description = input('Enter the description of the task: ')
     due_date = input('Enter the due date of the task (e.g 03 Mar 2023): ').lower().strip()
     date_format = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'] 
     due = due_date.split(' ')

     #This loop is executed when the user does not input enough information for the date
     while len(due) != 3 :
         print('invalid date format')
         due_date = input('Enter the due date of the task (e.g 03 Mar 2023): ').lower().strip()
         due = due_date.split(' ')

     #This while loop is executed when the user inputs the incorrect date format    
     while due[1] not in date_format or int(due[0]) > 31 or len(due[2]) != 4 or len(due[0]) != 2:
         print('invalid date format')
         due_date = input('Enter the due date of the task (e.g 03 Mar 2023): ').lower().strip()
         due = due_date.split(' ')
     
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

#==========================================================================================================================================
#the view_all function allows a user to view all the tasks
def view_all():
    lines = open('tasks.txt', 'r+')
    usertasks = lines.readlines()

        #loop to allows the tasks to be printed in user_friendly manner
    for x in range(len(usertasks)):
        sentence = usertasks[x].split(', ')
        sentence1 = f"\nTask: {sentence[1]}\nAssigned to: {sentence[0]}\nDate assigned: {sentence[4]}\nDue Date: {sentence[3]}\nTask complete?: {sentence[5]}\nTask description: {sentence[2]} "    
        print(sentence1)
           
#============================================================================================================================================
#the view_mine function to view and/or modify the details of the tasks of the current logged in user
def view_mine():
    lines = open('tasks.txt', 'r+')
    usertasks = lines.readlines()
    #user names are extracted in the tasks.txt file and stored in the names variable
    names = []
    
    for u in range(len(usertasks)):
        task = usertasks[u].split(', ')
        names.append(task[0])

    #The information of the user's tasks is extracted based on the on the index of the username in the tasks.txt file
    task_number = []
    #for loop to allow the user to view all the tasks assigned to them
    for user_id in range(len(names)):
        if user_name == names[user_id]:
            output = usertasks[user_id].split(', ')
            print(f'\nTASK {user_id}')
            task_number.append(user_id)
            output_final = f"Task: {output[1]}\nAssigned to: {output[0]}\nDate assigned: {output[4]}\nDue Date: {output[3]}\nTask complete?: {output[5]}\nTask description: {output[2]}\n "
            print(output_final)

    #The specific task variable allows the user to select a task they would like to access         
    specific_task = int(input('Which task do you want to access(e.g. TASK 3 is 3),(-1 to return to menu) : '))

    #This loop is executed if the user enters a task number that is not displayed on the screen
    while specific_task not in task_number:
        #allows the user to return to the main menu if they input -1
        if specific_task == -1:
            print('\nBack to main menu')
            break
        else:
            print('Invalid task! Try again')
            specific_task = int(input('Please enter the correct task number(e.g. TASK 3 is 3),(-1 to return to menu): '))
    
    #this prints the selected task
    while specific_task in task_number:
        spec_task =  usertasks[specific_task].split(', ')  
        task_specs = f"Task: {spec_task[1]}\nAssigned to: {spec_task[0]}\nDate assigned: {spec_task[4]}\nDue Date: {spec_task[3]}\nTask complete?: {spec_task[5]}\nTask description: {spec_task[2]}\n "
        print('\nRequested task')
        print(task_specs)
        
        #prompts user to input an action they would like to take with their selected task
        task_edit = input('Do you want to edit or mark the task as complete? (enter complete or edit): ').lower()

        #this loop ensures user enters the correct option
        #Based on the user input, the task will be edited or marked as complete
        while  task_edit != 'complete' and task_edit != 'edit':
            print("Invalid input")
            task_edit = input('Do you want to edit or mark the task as complete? (enter complete or edit): ').lower()
        else:
            #marks the task as complete then the choice is reflected in the tasks.txt file
            if task_edit == 'complete':
                file = open('tasks.txt', 'r')
                line = file.readlines()
                edit_line = line[specific_task].split(', ')
                edit_line[5] = 'Yes\n'
                line[specific_task] = ', '.join(edit_line)
                file = open('tasks.txt', 'w')
                for x in line:
                    file.write(x)
                break
            #this allows user to make changes to the task and changes are reflected in the tasks.txt file
            #only user name and due date are changed
            elif task_edit == 'edit':
                file = open('tasks.txt', 'r')
                line = file.readlines()
                edit_line = line[specific_task].split(', ')
                user_change = input('Enter new user for the task: ')
                
                while user_change not in user:
                    user_change = input('User does not exist! Please enter a correct username: ')

                new_date = input('Enter new due date: ')
                edit_line[0] = user_change
                edit_line[3] = new_date
                line[specific_task] =', '.join(edit_line)
                file = open('tasks.txt', 'w')
                for x in line:
                    file.write(x)
                break

#========================================================================================================================================
#The overview function allows the user to generate files with all the statistics related to the tasks.
def overview():
    #task-overview file generation
    #reads data from the tasks.txt file
    text = open('tasks.txt', 'r')
    num_text = text.readlines()
    num_tasks = len(num_text)
    complete = 0
    day = []

    #for loop which identifies tasks that are complete and incomplete
    for i in range(len(num_text)):
        sentence = num_text[i].split(', ')

        #This is executed if the task is completed
        if sentence[5].strip() == 'Yes':
            complete += 1

        #this is executed when a task is incomplete        
        else:
            now = datetime.now() #current date
            day.append(sentence[3])
            overdue = 0
            #loop to identify tasks that are overdue by comparing the due date and the current date
            for k in range(len(day)):
                date = f'{day[k]} 00:00:00' #due date

                if now > datetime.strptime(date, "%d %b %Y %H:%M:%S"):
                    overdue+=1
    #These are the required parameters which will be written to the task_overview text file        
    t1=(f'Total number of tasks: {num_tasks}')           
    t2=(f'Tasks complete: {complete}')
    t3=(f'Tasks incomplete: {num_tasks - complete}')
    t4=(f'Tasks overdue: {overdue}')
    t5=(f"Percentage of tasks incomplete: {round(((num_tasks - complete)/num_tasks)*100,2)}%")
    t6=(f'Percentage of tasks overdue: {round((overdue/num_tasks)*100,2)}%')
    task_overview = open("task_overview.txt",'w')
    task_overview.write(f'\n{t1}\n{t2}\n{t3}\n{t4}\n{t5}\n{t6}\n')
    
    #reads data from the user.txt file
    registered = open('user.txt', 'r')
    registered_users = registered.readlines()
    registered_num = len(registered_users)
    
    #User_overview file generation 
    #reads data from the tasks.txt file
    user_reg = open('tasks.txt', 'r')
    users_reg = user_reg.readlines()
    names =[]
    user_overview = open('user_overview.txt', 'w') 
    #loop to store user names
    for u in range(len(users_reg)):
        task = users_reg[u].split(', ')
        names.append(task[0])

       
    #The tasks information is extracted based on the on the index of the username in the tasks.txt file
    #This loop identifies the tasks for each user name
    register_user = []
    for w in range(len(registered_users)):
        reg = registered_users[w].split(', ')
        register_user.append(reg[0])
        #This is executed if user name has a task assigned to them
        if register_user[w] in names:
             user_task = []
             user_due = []
             user_complete = 0
             #for loop to determine the status of all the tasks assigned to the user
             for x in range(len(names)):
                #The statements identify the complete and incomplete tasks of the user
                if register_user[w] == names[x]:
                    user_task.append(names[x])
                    task2 = users_reg[x].split(', ')
                    if task2[5].strip() == 'Yes':
                        user_complete +=1
                    #for incomplete tasks    
                    else:
                        user_due.append(task2[3])
                        overdue_user = 0
                        #loop to identify the number of tasks that  are overdue  and not complete
                        for k in range(len(user_due)):
                            now = datetime.now()
                            user_date = f'{user_due[k]} 00:00:00'
                            if now > datetime.strptime(user_date, "%d %b %Y %H:%M:%S"):
                                overdue_user+=1

             #These are the required parameters which are written to the user  overview file
             u0 = f'\nUsername: {register_user[w]}'
             u1=f'Total number of users registered: {registered_num}'
             u2=f'Total number of tasks: {num_tasks}'
             u3=f'Number of tasks assigned to user: {len(user_task)}'
             u4=f'Percentage of tasks assigned to user: {round(100*len(user_task)/num_tasks,2)}%'
             u5=f'Percentage of tasks completed by user: {round(100*user_complete/len(user_task),2)}%'   
             u6=f'Percentage of tasks that must still be completed by user: {round(100*(len(user_task)- user_complete)/len(user_task),2)}%'       
             u7=f'Tasks overdue by user: {round(100*overdue_user/len(user_task),2)}%'
             user_overview.write(f'\n{u0}\n{u1}\n{u2}\n{u3}\n{u4}\n{u5}\n{u6}\n{u7}\n')  

        #executed if a user does not have a task assigned to them                  
        else:
            u8 = ('User does not have any tasks assigned yet!')     
            user_overview.write(f'\nUsername: {register_user[w]}\n{u8}\n')  

#============================================================================================================================================        
#display_stats function to display all statistics related to the tasks. Only the admin can acces.
def display_stats():
    #Only allows the admin user to access the stastistics
    if user_name == 'admin':
            #extracts data from the task_overview.txt file
            print('Task overview.')
            info = open('task_overview.txt', 'r')
            info_lines = info.readlines()
            for x in range(len(info_lines)):
                print(info_lines[x])

            print('\n')
            print('User overview')
            #extracts data from the task_overview.txt file    
            user_data = open('user_overview.txt', 'r')
            data_lines = user_data.readlines()
            for i in range(len(data_lines)):
                print(data_lines[i])    

    else:
            print('\n')
            print('You are not authorised to view this menu option!')
#====================================================================================================================================
#=====importing libraries===========
#Information from the text files is open and read 
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
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

#if statement to allow the user to register a new user
#it only allows the admin user to register new users
 
    if menu == 'r':
        pass
        reg_user()  
            
    #This statement only allows the admin user to view statistics about the users and tasks
    elif menu == 'gr':
        #overview is called
        overview()
    
    elif menu == 'ds':
        #display_stats function is called
        display_stats()

    #This allows a task to be assigned to a user
    elif menu == 'a':
        pass
        #add_task function is called
        add_task()
    
    #this allows the user to view all the tasks
    elif menu == 'va':
        pass
        #view_all function is called
        view_all()

    #this allows the current user that is logged in to view their task.
    elif menu == 'vm':
        pass
        #view_mine function is called
        view_mine()
    #Allows the user to exit the program
    elif menu == 'e':
        print('Goodbye!!!')
        #exit function is called
        exit()
    else:
        print("You have made a wrong choice, Please Try again")




