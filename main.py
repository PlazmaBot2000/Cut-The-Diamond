import subprocess
import os
import json

MaxTask = 2








#============================== Run command function ===================================
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"{e.stderr}"







#================================= Menu function =======================================
def menu(n, type):
    print('Menu:')
    if type == 'm':
        print('    Do the next task - №' + str(n+1) + ' (1)')
    elif type == 'f':
        print('    Try again (1)')
    print('    Select another task (2)')
    print('    Exit (3)')
    Select = int(input('Select:'))
    match Select:
        case 1:
            try:
                if type == 'm':
                    task(n+1)
                elif type == 'f':
                    task(n)
            except:
                print('There isn\'t task associated with this number')
                menu(n, 'm')
        case 2:
            try:
                task(int(input('Enter task number: ')))
            except:
                print('There isn\'t task associated with this number')
                menu(n, 'm')
        case 3:
            exit






#================================= Task function =======================================
def task(n):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    task_number = str(n)
    task_name = tasks[task_number]['name']
    task_start_cmd = tasks[task_number]['startcmd']
    task_result = tasks[task_number]['result']
    os.system('clear')
    print('Selected task: ' + task_number + ' ' + task_name)
    print('Result: ' + task_result)

    command_input = task_start_cmd + input('Command: ' + task_start_cmd)
    output = run_command(command_input).replace("\n", "")
    print('Output: ' + output)


    if output == task_result:
        print('Congratulations! You solved task №' + task_number + ' ' + task_name)
        menu(n, 'm')
    else:
        print('No')
        menu(n, 'f')







#====================================== Main ===========================================
os.system('clear')
menu(0,'m')
