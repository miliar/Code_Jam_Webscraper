def solve(c, f, x):
    rate = 2.0
    buildTime = c/rate
    buildTotalTime = 0.0
    totalTime = 0
    newTotalTime = x/rate
    
    while 1:
        rate += f
        buildTotalTime += buildTime
        buildTime = c/rate
        totalTime = newTotalTime
        newTotalTime = buildTotalTime + x/rate
        if newTotalTime > totalTime: return str(totalTime)
    

f_in = open("in.txt")
f_out = open("out.txt","+w")
n_cases = int(f_in.readline())

print(str(n_cases) + " test cases!")

for case_nr in range(n_cases):
    
    (c, f, x) = (float(x) for x in f_in.readline().split(" "))
    print(c, f, x)
    ans = solve(c, f, x)
    
    print("Case #" + str(case_nr+1) + ": " + ans + "\n")
    f_out.write("Case #" + str(case_nr+1) + ": " + ans + "\n")

f_in.close()
f_out.close()
