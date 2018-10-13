T = int(input())

def solve(case):
    farmC, farmOutput, win = [float(x) for x in input().split()]
    
    # stop buying farms when time = win/input < (win+farm)/(input+farmOutput)

    time = 0
    inp = 2.0

    while win/inp > win/(inp+farmOutput) + farmC/inp:
        time += farmC/inp
        inp += farmOutput
        #print("Bought farm, time = {}".format(time))
    #print("Stop spending, wait for money, time = {}".format(time))
    time += win/inp

    print("Case #{}: ".format(case), end="")
    print(time)
    

for t in range(T):
    solve(t+1)
