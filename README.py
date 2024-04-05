# python-project
def add_task():
    task=input("Please Enter the task: ")
    task_details= {"task":task,"status": False}
    tasks.append(task_details)
    print("The task added successfuly✔")

def mark_task():
    incompleted_tasks=[]
    for task in tasks:
        if not task["status"]:
           incompleted_tasks.append(task)
    if incompleted_tasks:
      for x, task in enumerate(incompleted_tasks):
        print(f'{x+1}-{task["task"]}')
      choise=int(input("enter the number of completed task:"))
      incompleted_tasks[choise-1]["status"]=True
      print("task marked successfuly")
    else:
        print("All tasks are finished")
def view_task():
    if tasks:
        for x, task in enumerate(tasks):
            if task["status"]:
                status_again="✔"
            else:
                status_again="❌"
            print(f"{x+1}.{task['task']}{status_again}")
    else:
        print("there are no tasks to view")
def remove():
    del_task=int(input("enter number of task you wanna remove"))
    if del_task <= len(tasks):
        #del tasks[del_task - 1]
        tasks.remove(tasks[del_task -1])
        print("the task removed successfuly✔")
    else:
        print("Invalid number")
   


task_management= """1- view all tasks:
2- add new task:
3- mark task:
4-remove task:
5- Exit"""
print(task_management)
tasks=[]
while True:
    choose= input("Please enter a number:")
    if choose =="1":
        view_task()
        
    elif choose =="2":
        add_task()
    elif choose=="3":
        mark_task()
    elif choose=="4":
        remove()
     elif choose=="5":
        break
    else:
        print("invalid input")
    elif choose=="5":
        break
    else:
        print("invalid input")
        continue
