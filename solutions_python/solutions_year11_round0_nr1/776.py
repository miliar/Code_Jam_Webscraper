with open('A-large.in') as f:
    cases = int(f.next())
    caseNum = 1
    for line in f:
        moves = 0
        oindex = 1
        bindex = 1
        data = line.split()
        N = int(data[0])
        pdata = []
        order = 0
        for i in range((len(data)-1)/2):
            x = 2*i+1
            pdata.append((data[x],int(data[x+1]),order))
            order += 1
        oTasks = []
        bTasks = []
        for task in pdata:
            if task[0]=='O':
                oTasks.append((task[1],task[2]))
            else:
                bTasks.append((task[1],task[2]))
        while len(oTasks)+len(bTasks)>0:
            if len(oTasks)>0:
                oTask = oTasks[0]
            else:
                oTask = (oindex,float('inf'))
            if len(bTasks)>0:
                bTask = bTasks[0]
            else:
                bTask = (bindex,float('inf'))
            if oindex!=oTask[0]:
                oindex += (oTask[0]-oindex)/abs(oTask[0]-oindex)
            elif oTask[1]<bTask[1]:
                del oTasks[0]
            if bindex!=bTask[0]:
                bindex += (bTask[0]-bindex)/abs(bTask[0]-bindex)
            elif bTask[1]<oTask[1]:
                del bTasks[0]
            moves += 1
        print "Case #"+str(caseNum)+": "+str(moves)
        caseNum += 1
