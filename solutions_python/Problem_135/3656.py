import sys

def readcandidates():
    choice1 = int(sys.stdin.readline().strip())
    for before in range(1,choice1):
        sys.stdin.readline()
    candidates = set(sys.stdin.readline().strip().split())
    for after in range(choice1+1,5):
        sys.stdin.readline()
    return candidates

T = int(sys.stdin.readline().strip())
for i in range(1, T+1):
    common = readcandidates() & readcandidates()
    print "Case #" + str(i) + ":",
    if len(common) == 1:
        print list(common)[0]
    elif len(common) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
