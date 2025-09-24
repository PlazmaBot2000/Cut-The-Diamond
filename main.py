import subprocess
import json



#============================== Functions ===================================
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"{e.stderr}"



#============================ Load JSON file ================================
with open('tasks.json', 'r') as file:
    tasks = json.load(file)



#============================= Parse JSON ===================================
task_number = input('Enter task number: ')
task_name = tasks[task_number]['name']
task_start_cmd = tasks[task_number]['startcmd']
task_result = tasks[task_number]['result']
print('Selected task: ' + task_number + ' ' + task_name)
print('Result: ' + task_result)



#========================= Enter and run command ============================
command_input = input('Command: ' + task_start_cmd)
output = run_command(command_input).replace("\n", "")
print('Output: ' + output)



#============================= Check answer =================================
if output == task_result:
    print('Congratulations! You solved task №' + task_number + ' ' + task_name + '.')
else:
    print('No')
