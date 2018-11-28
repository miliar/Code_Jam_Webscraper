def solve():
    c,f,x = [float(x) for x in raw_input().split()]
    rate = 2.0
    currentTime = 0
    time = x/rate
    solution = False
    while not solution:
        totalTime = currentTime + c/rate + x/(rate+f)
        if totalTime > time:
            print time
            solution = True
        else :
            currentTime = currentTime + c/rate
            time = totalTime
            rate = rate + f
    
    

if __name__ == "__main__":
    i = int(raw_input())
    for _i in range(i):
        print "Case #" + str(_i + 1) + ":",
        solve()
