import sys

sys.stdin = open("A-small-attempt2.in", "r")
sys.stdout = open("A-small-attempt2.txt", "w")

t = int(raw_input())

m = []

for test in xrange(t):
    m = []
    t -= 1
    x = int(raw_input())
    for i in xrange(4):
        m.append(map(int, raw_input().split()))
#         print(m[i])
    
    row = m[x-1]
    
    y = int(raw_input()) - 1
    m = []
    for i in xrange(4):
        m.append(map(int, raw_input().split()))
#         print(m[i])
    
    num = -1 
    # -1 - number not found - cheating 
    # -2 - two numbers in the same row - bad magician
    
    newRow = m[y]
    for searchCol in xrange(4):
        for j in xrange(4):
            if newRow[searchCol] == row[j]:
                if num > 0:
                    num = -2
                    break
                else:
                    num = row[j]
        if num == -2:
            break
    
    prefix = "Case #" + str(test+1)
    if num == -1:
        print(prefix + ": Volunteer cheated!")
    elif num == -2:
        print(prefix + ": Bad magician!")
    else:
        print(prefix + ": " + str(num))
    