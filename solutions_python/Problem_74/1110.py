def solve(tasks):
    nTasks = len(tasks)
    places = {"O": 1, "B": 1}
    clocks = {"O": 0, "B": 0}

    for t in range(0,nTasks,2):

        curBot = tasks[t]
        otherBot = "B" if curBot == "O" else "O"
        k = int(tasks[t+1])
        steps=abs(places[curBot] - k) + 1
        clocks[curBot] = max (clocks[curBot] + steps,clocks[otherBot]+1)
        places[curBot]=k
            
    return max(clocks["O"],clocks["B"])


t = int(input())
for t_no in range(1,t+1):
    tasks = raw_input().split(" ")[1:]
    print "Case #%d: %d" % (t_no,solve(tasks))
