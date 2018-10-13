import re
def istidy(x):
    prev = 0
    for c in x:
        if prev > int(c):
            return False
        prev = int(c)
    return True

t = int(input())
for i in range(t):
    n = int(input())
    s = str(n)
    while not istidy(s):
        #print("#")
        for j in range(len(s) - 1):
            #print(s)
            a = int(s[j])
            b = int(s[j+1])
            if a > b and a > 0:
                s = s[:j] + str(a - 1) + "9"*len(s[j+1:])
                break
        s = re.sub(r"^0+","",s)
        #print(s)
    print("Case #" + str(i+1) + ": " + s)
