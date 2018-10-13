fin  = open('cookie_input.txt','r')
fout = open('cookie_output.txt','w')

cases = int(fin.readline())

for c in range(cases):
    C,F,X = [float(x) for x in fin.readline().strip().split(' ')]

    farms = []
    time_to_obtain_farm = []
    rate = []
    time_goal =[]

    i = 0

    #print C, F, X

    while True:
        farms.append(i)

        if i == 0:
            time_to_obtain_farm.append(0)
            rate.append(2)
            time_goal.append((X/2))
        else:
            time_to_obtain_farm.append((C/rate[i-1]) + float(time_to_obtain_farm[i-1]))
            rate.append(2+F*farms[i])
            time_goal.append((X/rate[i]) + float(time_to_obtain_farm[i]))

        if i == 0:
            i = i + 1
            continue

        #make sure rate is decreasing
        if time_goal[i] < time_goal[i-1]:
            i = i + 1
            continue
        else:
            #print "Case #" + str(c + 1) + ": " + str(time_goal[i - 1])
            fout.write("Case #" + str(c + 1) + ": " + str(time_goal[i - 1]) + "\n")
            break

        i = i + 1
