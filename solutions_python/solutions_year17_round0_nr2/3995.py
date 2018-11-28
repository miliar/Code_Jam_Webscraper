

T = input()

def isSorted(s):
    for i in range(1,len(s)):
        if(s[i] < s[i-1]):
            return False
    return True

for i in range(0, int(T)):
    N = int(input())
    for j in range(N, 0, -1):
        js = str(j)
        if(len(js)==0):
            print("Case #"+str(i+1)+": "+js)
            break
        else:
            if(isSorted(js)):
                print("Case #"+str(i+1)+": "+js)
                break

