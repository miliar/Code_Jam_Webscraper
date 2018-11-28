
def robots(filename):
    f = open(filename, "r")
    
    T = int(f.readline())
    
    missions = []
    for case in range(T):
        line = f.readline()
        seq = line.split()
        missions.append(seq)
        
    f.close()
    
    f = open(filename+".out", "w")
    
    for i in range(len(missions)):
        mission = missions[i]
    
        B = []
        O = []
        A = []
        
        N = int(mission[0])
        
        for task in range(1,N+1):
            robot = mission[2*task-1]
            button = int(mission[2*task])
            A.append((robot, button))
            if robot=="B":
                B.append(button)
            else:
                O.append(button)
                
        time = 0
        
        Opos = 1
        Bpos = 1
        Ofinished = False
        Bfinished = False
        while A<>[]:
            time = time+1
            (robot, button) = A[0]
            

            Bbutton = B[0] if B<>[] else 1
            Obutton = O[0] if O<>[] else 1
            

            if robot=="O" and Opos==button:
                A.pop(0)
                O.pop(0)
                if (Bpos>Bbutton):
                    Bpos -=1
                elif(Bpos<Bbutton):
                    Bpos +=1
            elif robot=="B" and Bpos==button:
                A.pop(0)
                B.pop(0)
                if (Opos>Obutton):
                    Opos -=1
                elif(Opos<Obutton):
                    Opos +=1
            else:
                if (Bpos>Bbutton):
                    Bpos -=1
                elif(Bpos<Bbutton):
                    Bpos +=1
                if (Opos>Obutton):
                    Opos -=1
                elif(Opos<Obutton):
                    Opos +=1
                    
        print "Case #"+str(i+1)+": "+str(time)
        f.write("Case #"+str(i+1)+": "+str(time) + "\n")
        
    f.close()
                
                
            
            
            
            