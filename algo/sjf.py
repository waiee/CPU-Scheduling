def ganttChart(bar, time, processName):
    print("Gantt Chart: \n")
    print("*--------", end="")
    for i in range(bar-1):
        print("---------",end="")
    print("*")

    for i in range(bar):
        print(f'{("|   " + processName[i] +"  "):9.7}',end="")
    print("|")

    print("*--------",end="")
    for i in range(bar-1):
        print("---------",end="")
    print("*")

    for i in range(len(time)):
        print(f'{(str(time[i])+"       "):9.3}',end="")
    time.pop(0)
    print("\n")

def printProcess(id, bt, time, info):
    for i in range(size):
        print("P" + str(id[i]) + "(" + str(bt[i]) + ")")
        print("Finishing Time: " + str(time[i]) + " second")
        print("Turnaround Time: " + str(info[i]['turnaround_time']) + " second")
        print("Waiting Time: " + str(info[i]['waiting_time']) + " second")
        print("")

#Sort by arrival time
def sort_param(e):
    return e['arrival_time']

#Sort by burst time
def sort_burst(e):
    return e['burst_time']

# User insert number of process
print("[Non-Preemptive SJF] \n")
while True:
    n = int(input("Enter number of processes: "))
    if n < 3 or n > 10:
        print("Please enter number from 3-10.")
    else:
        break
print("")

#Define
size = n
info = []
copy_info = []
final_info = []
totalTime = 0

#User input
for i in range(size):
    process_info = {}
    # print("[P" + str(i) + "]")
    process_info['id'] = str(input("Enter Process Name: "))
    process_info['burst_time'] = int(input("Enter Burst Time: "))
    process_info['arrival_time'] = int(input("Enter Arrival Time: "))
    info.append(process_info)
    totalTime += info[i]['burst_time']
    process_info['turnaround_time'] = totalTime-process_info['arrival_time']
    process_info['waiting_time'] = process_info['turnaround_time']-process_info['burst_time']
    print("")

# Menu
print("---------------------------------------------")
print("{:<15} {:<15} {:<15}".format('Process', 'Burst Time', 'Arrival Time'))
for i in range(size):
    p = info[i]
    print("{:<15} {:<15} {:<15}".format(
        p['id'], p['burst_time'], p['arrival_time']))
print("---------------------------------------------")

# Algorithm
time = 0
timeFrame = [0]
finalID = []
finalBt = []
last_info = []
totalTt = 0
totalWt = 0
avTt = 0
avWt = 0

info.sort(key=sort_param)
for i in range(totalTime): 
    for j in range(size): 
        if info[j]['arrival_time'] == i:
            copy_info.append(info[j])
        else:
            copy_info.sort(key=sort_burst)
            for n in range(len(copy_info)):
                final_info.append(copy_info[n])
            copy_info.clear()

for i in range(size):
    print_info = final_info[i]
    wt = print_info['waiting_time']
    tt = print_info['turnaround_time']
    arr = print_info['arrival_time']
    bt = print_info['burst_time']

    time += print_info['burst_time']
    timeFrame.append(time)
    finalID.append(print_info['id'])
    finalBt.append(print_info['burst_time'])

    #Turnaround time
    tt=time-arr
    totalTt += tt
    avTt = float(totalTt/size)

    #Waiting Time
    wt=tt-bt
    totalWt += wt
    avWt = float(totalWt/size)

#Output
print("\n")
ganttChart(size, timeFrame, finalID)
# printProcess(finalID, finalBt, timeFrame, final_info)
print("Total Turnaround Time: " + str(totalTt))
print("Average Turnaround Time: " + str(avTt))
print("")
print("Total Waiting Time: " + str(totalWt))
print("Average Waiting Time: " + str(avWt) + "\n")