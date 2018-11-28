T = int(input())
num = T

def tidy(s):
    if len(s) == 1:
        return True
    for i in range(1, len(s)):
        if int(s[i - 1]) > int(s[i]): return False
    return True

while T:
    T -= 1
    case = num - T
    N = int(input())
    for i in range(N, 0, -1):
        if tidy(str(i)):
            print("Case #" + str(case) + ": " + str(i))
            break
