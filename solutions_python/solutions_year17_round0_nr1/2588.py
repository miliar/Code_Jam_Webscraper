flip = 0
with open('./A.in','r') as f:
    cases=int(f.readline())
    lines=f.readlines()

inputs=[]
def convert(l, k, idx):
    if l[idx] == '-':
        global flip
        flip = flip + 1 
        for i in range(idx, idx + k):
            if l[i] == '-':
                l[i] = '+'
            else: 
                l[i] = '-'
    return l

def check(l):
    for j in range(0, len(l)):
        if l[j] != '+':
            return False
    return True

for i in range(cases):
    flip = 0
    [hotdog, number] = (lines[i].split(' '))
    k = int(number)
    l = list(hotdog)

    for j in range(0, len(l) - k + 1):
        l = convert(l, k, j)

    if (not check(l)):
        print "Case #" + str(i+1) + ": " + "IMPOSSIBLE"
    else:
        print "Case #" + str(i+1) + ": " + str(flip)
