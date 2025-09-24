import subprocess
import os
import json
import bashlex

MaxTask = 2



#============================== Run command function ===================================
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"{e.stderr}"



#================================= Menu function =======================================
def fail_menu(n):
    print('Menu:')
    print('    Try again (1)')
    print('    Select another task (2)')
    print('    Exit (3)')
    Select = int(input('Select:'))
    match Select:
        case 1:
            task(n)
        case 2:
            try:
                task(int(input('Enter task number: ')))
            except:
                print('There isn\'t task associated with this number')
        case 3:
            exit

def main_menu(n):
    print('Menu:')
    print('    Do the next task (1)')
    print('    Select another task (2)')
    print('    Exit (3)')
    Select = int(input('Select:'))
    match Select:
        case 1:
            try:
                task(n+1)
            except:
                print('There isn\'t task associated with this number')
        case 2:
            try:
                task(int(input('Enter task number: ')))
            except:
                print('There isn\'t task associated with this number')
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
    #print(bashlex.parse(command_input))
    output = run_command(command_input).replace("\n", "")
    print('Output: ' + output)


    if output == task_result:
        print('Congratulations! You solved task №' + task_number + ' ' + task_name)
        main_menu(n)
    else:
        print('No')
        fail_menu(n)







#====================================== Main ===========================================
main_menu(0)
