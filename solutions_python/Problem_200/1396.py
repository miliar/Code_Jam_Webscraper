import sys

def tidy(s):
    if (len(s) == 1):
        return True
    for i in range(len(s)-1):
        if (int(s[i]) > int(s[i+1])):
            return False
    return True

testCases = int(input())

for testCase in range(1, testCases + 1):
    s = raw_input()
    # print "+"+s
    k = len(s)-1
    while (not tidy(s)):
        # print s
        if (k==0):
            s = "9"*(len(s)-1)
        elif (int(s[k-1]) > int(s[k])):
            if (int(s[k-1]) != 0):
                s = list(s)
                s[k-1] = str(int(s[k-1])-1)
                for i in range(k,len(s)):
                    s[i] = str(9)
                s = "".join(s)
            else:
                s = s[:k]+"9"*(k-len(s)-1)
        else:
            k-=1
    if (s[0] == "0"):
        s = s[1:]
    print("Case #" + str(testCase) + ": " + s)