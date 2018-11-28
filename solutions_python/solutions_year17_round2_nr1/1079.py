f = open("A-large (2).in","r").readlines()
g = open("A-large-out.txt","w")
testcases = int(f[0])
line_no = 1

for j in range(1,testcases+1):
    
    desti, horses = list(map(int,f[line_no].strip().split()))
    times = []
    for i in range(horses):
        
        line_no += 1
        start, speed = list(map(int,f[line_no].strip().split()))
        time = round((desti - start)/speed, 7)
        times.append(time)
    
    mins = max(times)
    ans = round(desti/mins, 7)
    line_no += 1
    
    g.write("Case #"+ str(j) + ": " + str(ans) + "\n") 