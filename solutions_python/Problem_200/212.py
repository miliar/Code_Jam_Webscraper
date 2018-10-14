def compute(num):
    for i in range(len(num)-1, 0, -1):
        if num[i-1] > num[i]:
            num[i-1] -= 1
            for j in range(i, len(num)):
                num[j] = 9
    return int("".join([str(d) for d in num]))
            
                                    
T = int(input())
for t in range(1,T+1):
    num = [int(c) for c in input()]
    print("Case #%d:"%t, compute(num)) 
