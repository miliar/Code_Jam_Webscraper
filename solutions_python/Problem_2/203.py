import sys,math
def time(s):
    s = map(int,s.split(":"))
    return s[0]*60+s[1]

lines = sys.stdin.readlines()
it = iter(lines)
num = int(it.next())
for i in range(num):
    case = 1+i
    turn_time = int(it.next())
    num_ab,num_ba = map(int,it.next().split())
    t_ab,t_ba = [],[]
    for j in range(num_ab):
        t_ab.append(map(time,it.next().split()))
    for j in range(num_ba):
        t_ba.append(map(time,it.next().split()))
    t = [(tim,"a") for tim in t_ab]+[(tim,"b") for tim in t_ba]
    t.sort(key=lambda a:a[0])
    need = [0,0]
    at = [[],[]]
    for train in t:
        if train[1] == "a":
            a,b = 0,1
        else:
            b,a = 0,1
        #add to destination
        at[b].append(train[0][1]+turn_time)
        old = None
        for tim in at[a]:
            if tim <= train[0][0]:
                   old = tim
        if old:
            at[a].remove(old)
        else:
            need[a] += 1
    print "Case #"+str(case)+": "+str(need[0])+" "+str(need[1]) 
                   
        
