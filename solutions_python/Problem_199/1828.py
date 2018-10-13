
def leftmost(pan):
    for i in range(len(pan)):
        if pan[i] == '-':
            return i
    return 'none'
infile = open('A-large.in','r')
t = infile.readline()
outfile = open('q1outlarge.txt','w')
line = str(infile.readline().strip())
count = 1
minflips = 100
def determine(line):
    global minflips
    st = line.split()
    pancakes = st[0]
    size = int(st[1])
    k = size
    minflips = len(pancakes)
    pan = pancakes
    leftM = leftmost(pan)
    #if(pan.count('-') < k):
    #    if pan.count('-') % 2 == 1:
    #        if k % 2 == 1:   
    #            print("Imp cond true")
    #            return "IMPOSSIBLE"
    #    else:
    #        if k % 2 == 1:
    #            print("Imp cond true")
    #            return "IMPOSSIBLE"
    test = str(pan[:])
    testM = leftM
    flips = 0
    while testM != 'none':
        test = flip(test,k,testM)
        testM = leftmost(test)
        flips += 1
        #print(test)
        if test == 'Cant flip' or flips > len(test):
            #print("LFLIP")
            return "IMPOSSIBLE"
    minflips = flips
    return minflips
    if leftM != 'none':
        for i in range(len(pan)-int(k)-leftM+1):
            if contains(pan,leftM+i,k):
                tryflip(flip(pan,k,leftM+i),k,1)
    else:
        return 0
    return minflips
def tryflip(pan,k,c):
    global minflips
    if c > minflips:
        return
    if leftmost(pan) == 'none':
        minflips = c
        return
    #print(pan)
    leftM = leftmost(pan)
    for i in range(len(pan)-int(k)-leftmost(pan)+1):
        if contains(pan,leftM+i,k):
            tryflip(flip(pan,k,leftM+i),k,c+1)
def contains(pan,pos,k):
    for i in range(k):
        if pan[pos+i] == '-':
            return True
    return False
def flip(p,k,pos):
    if len(p) - pos < k:
        return "Cant flip"
    newpan = ""
    if pos > 0:
        newpan = p[0:pos]
    for i in range(k):
        if p[pos+i] == '+':
            newpan += '-'
        else:
            newpan += '+'
    if len(p) > pos + k:
        newpan += p[pos+k:]
    return newpan
while line != "":
    outfile.write("Case #"+str(count)+": "+str(determine(line))+"\n")
    print("just done "+str(line))
    line = str(infile.readline())
    count += 1
outfile.close()
print('done')

