DEBUG=0
import math

def printd(*arg):
    if DEBUG == 1:
        print("---",arg)

def surface_panckes(pancakes):
    result = 0
    if len(pancakes) >=0:
        pancakes = sorted(pancakes)
        for p in pancakes:
            result += 2*math.pi*p[0]*p[1]
        result += math.pi*(pancakes[len(pancakes)-1][0]**2)
    return result

t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    n,k =  [int(s) for s in input().split(" ")]
    printd("n,k:",n,k)
    pancakes = []
    heights=[]
    for i in range(n):
        r,h = [int(s) for s in input().split(" ")]
        pancakes.append([r,h])
        heights.append(h)
    printd("pancakes:",pancakes)
    result = 0
    if n > k:
        sorted_pancakes = sorted(pancakes, key=lambda p: math.pi*p[0]*p[1])
        sorted_pancakes.reverse()
        printd("sorted pancakes:",sorted_pancakes)
        pancakes_in = sorted_pancakes[:k-1]
        printd("pankaces_in",pancakes_in)
        pancakes_out = sorted_pancakes[k-1:]
        printd("pankaces_out",pancakes_out)
        max = 0
        for p_out in pancakes_out:
            printd("p_out",p_out)
            printd("pancakes_in",pancakes_in)
            p = pancakes_in.copy()
            p.append(p_out)
            printd("p:",p)
            surface = surface_panckes(p)
            if surface > max:
                max = surface
        result = max
    else:
        result = surface_panckes(pancakes)
    print("Case #{}: {}".format(case_num,result))
    
    
