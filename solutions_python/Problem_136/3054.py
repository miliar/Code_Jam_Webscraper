n = raw_input()

input = n.split()

mylist = zip(*(iter(input[1:]),) * 3)


# C = factory cost
# F = gain from factory
# X = goal
case = 1
for (C,F,X) in mylist:
        C = float(C)
        F = float(F)
        X = float(X)
        gain = 2
        time = 0
        oldTime = X / gain
        while True:
                waitingTime = C / gain
                #print oldTime, ">=", time + (waitingTime + (X / (gain+F))) ,"=", time, "+", waitingTime, "+" ,X, "/" ,gain,"+",F
                if(oldTime > time + (waitingTime + (X / (gain+F)))):
                        oldTime = time +(waitingTime + (X / (gain+F)))
                        time += waitingTime
                        gain += F
                        #print time, oldTime, waitingTime
                else:
                        print "Case #" + str(case) +":", oldTime
                        case += 1
                        break
                
	
       

