people_list = []
stalls_list=[]
k= []
output=open('output_large.in', 'w+')
dataFile = open("C-large.in", 'r')
rows = dataFile.readline()
for line in dataFile:
    stalls_list.append(int(line.split(" ")[0]))
    people_list.append(int(line.split(" ")[1]))

for i in range(len(stalls_list)):
    stalls=stalls_list[i]
    people = people_list[i]
    windows=[stalls]
    print i
    windows_count = [1]
    current_window = max(windows)
    j = people
    while j>0 and current_window>0:
        #print str(j) + " " +str(windows) + " " + str(windows_count)
        current_window=max(windows)
        current_window_count=windows_count[windows.index(current_window)]
        windows.remove(current_window)
        windows_count.remove(current_window_count)
        if current_window % 2 == 0:
            add_window=current_window/2
            if(add_window in windows):
                windows_count[windows.index(add_window)]+= current_window_count
            else:
                windows.append(add_window)
                windows_count.append(current_window_count)

            add_window = current_window / 2 -1
            if (add_window in windows):
                windows_count[windows.index(add_window)] += current_window_count
            else:
                windows.append(add_window)
                windows_count.append(current_window_count)
        else:
            add_window = (current_window-1) / 2
            if (add_window in windows):
                windows_count[windows.index(add_window)] += (2*current_window_count)
            else:
                windows.append(add_window)
                windows_count.append(2*current_window_count)
        j = j-current_window_count

    output.write('Case #'+str(i+1)+': ')
    if current_window==0:
        output.write(str(current_window) + " " + str(current_window))
    else:
        if current_window % 2 == 0:
            output.write(str(current_window / 2) + " " + str((current_window / 2)-1))
        else:
            output.write(str((current_window-1) / 2) + " " + str((current_window-1) / 2))
    output.write('\n')

