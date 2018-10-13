infile = open('B-large.in','r')
t = infile.readline()
outfile = open('q1outlarge.txt','w')
line = str(infile.readline().strip())
count = 1
def determine(num):
    n = str(num)
    if n == 0:
        return '0'
    currentIndex = 0
    new = ''
    while currentIndex < len(n)-1 and int(n[currentIndex]) <= int(n[currentIndex+1]):
        new += n[currentIndex]
        currentIndex += 1
    if currentIndex < len(n)-1:
        new += str(int(n[currentIndex])-1)
        new += "".join(['9' for i in range(len(n)-currentIndex-1)])
    if currentIndex == len(n) - 1:
        new += n[currentIndex]
    while not isTidy(new):
        new = determine(new)
    if len(new) == 0:
        return '0'
    return trimz(new)
def trimz(st):
    s = str(st)
    if len(s) == 0:
        return ''
    c = 0
    while c < len(s) and s[c] == '0':
        c+=1
    return s[c:]
def isTidy(num):
    for dig in range(len(str(num))-1):
        if int(str(num)[dig]) > int(str(num)[dig+1]):
            return False
    return True
while line != "":
    outfile.write("Case #"+str(count)+": "+str(determine(line))+"\n")
    print("just done "+str(line))
    line = str(infile.readline().strip())
    count += 1
outfile.close()
print('done')
