count = int(raw_input())
lottery = []
case = []
for i in range(count):
    lottery.append(raw_input())

for i in range(count):
    arr = lottery[i].split()
    A = int(arr[0])
    B = int(arr[1])
    K = int(arr[2])
    poss = 0
    for old in range(A):
        for new in range(B):
            temp = old&new
            if temp < K:
                poss += 1

    case.append(poss)

for i in range(count):
    print "Case #"+str(i+1)+": "+str(case[i])
        
                
