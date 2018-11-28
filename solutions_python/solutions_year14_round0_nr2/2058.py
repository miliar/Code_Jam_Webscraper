def TimeToGoal(cps,X):
    return float(X/cps)

def TimeForFarm(cps,C):
    return float(C/cps)


##def BestTime(C,F,X,cps=2.0,i=0):
##    if TimeToGoal(cps,X)<=(TimeToGoal(cps+F,X)+TimeForFarm(cps,C)):
##        print(i)
##        return round(TimeToGoal(cps,X),7)
##    else:
##        i+=1
##        return TimeForFarm(cps,C) + BestTime(C,F,X,cps+F,i)

def BestTime(C,F,X):
    cps=2.0
    time = 0.0
    while (TimeToGoal(cps,X)>=(TimeToGoal(cps+F,X)+TimeForFarm(cps,C))):
        time+=TimeForFarm(cps,C)
        cps+=F
    time+=TimeToGoal(cps,X)
    return round(time,7)
           

def Main():
    out = ""
    f = open("B-large.in").read()
    f = f.split("\n")
    cases = int(f.pop(0))

    #print(cases)
    for case in range(1,cases+1):
        L = f.pop(0).split(" ")
        L = [float(i) for i in L]
        out+=("Case #"+str(case)+": "+str(BestTime(L[0],L[1],L[2])))
        if case!=cases: out+="\n"
        print("Case #"+str(case)+": "+str(BestTime(L[0],L[1],L[2])))
    text_file = open("out.txt", "w")
    text_file.write(out)
    text_file.close()
    #print(out)

Main()
