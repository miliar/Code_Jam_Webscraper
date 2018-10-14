import sys

def previousTidy(N):
    num = str(N)

    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            num = num[:i] + str(int(num[i]) -1) + '9'*(len(num) -i-1)
            num = str(previousTidy(int(num)))
            break
    return int(num)



f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    N = int(f.readline())
   
    result = previousTidy(N)
    
    print("Case #{0}: {1}".format(i+1, result))
f.close()