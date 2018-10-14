import sys

path = "test.in" if len(sys.argv) == 1 else sys.argv[1]
file = open(path, "r")
T = int(file.readline())

def simplify(s):
    q = []
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            q.append(s[i])
    if len(s) > 1 and s[len(s)-1] != s[len(s)-2]:
        q.append(s[len(s)-1])
    return q

for casenum in range(T):
    N = int(file.readline())
    s1 = file.readline().strip() + '-'
    s2 = file.readline().strip() + '-'

    i, j = 0, 0
    count = 0
    last_i, last_j = -1, -1
    result = True
    while True:
        while i < len(s1) and s1[i] == s1[i+1]:
            i += 1
        while j < len(s2) and s2[j] == s2[j+1]:
            j += 1
        if s1[i] != s2[j]:
            print("Case #{0}: {1}".format(casenum+1, "Fegla Won"))
            result = False
            break
        else:
            if last_i >= 0 and last_j >= 0:
                count += abs((i-last_i) - (j-last_j))
            else:
                count += abs(i - j)
            last_i = i
            last_j = j
            i += 1
            j += 1
        if s1[i] == '-' or s2[j] == '-':
            if s1[i] != s2[j]:
                print("Case #{0}: {1}".format(casenum+1, "Fegla Won"))
                result = False
            break
    if result:
        print("Case #{0}: {1}".format(casenum+1, count))
