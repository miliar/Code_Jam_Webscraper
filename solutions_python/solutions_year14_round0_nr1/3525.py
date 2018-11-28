import sys
sys.stdin = open("A.in")
sys.stdout = open("A.out","w")
T = input()
for i in range(T):
    print "Case #%d:"%(i+1),
    a = input()
    f1 = []
    for j in range(4):
        f1.append(set(raw_input().split()))
    b = input()
    f2 = []
    for j in range(4):
        f2.append(set(raw_input().split()))
    c = f1[a-1] & f2[b-1]
    #~ print c
    if (len(c)==1):
        print list(c)[0]
    elif (len(c)==0):
        print "Volunteer cheated!"
    else:
        print "Bad magician!"
    
