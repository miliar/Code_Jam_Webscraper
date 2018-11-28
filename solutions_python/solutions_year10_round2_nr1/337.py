
def makeDirect(li, di):
    count = 0
    #print li
    #print di
    for i in range(len(di)):
        try:
            li.index(di[0:i+1])
        except:
            li.append(di[0:i+1])
            count += 1
    return count

def splitString(li):
    newlist = []
    newlist = li.rstrip("\n").split("/")
    del newlist[0]
    return newlist
    
f = open("A-large.in")
case = int(f.readline())
string = ''
for k in range(case):
    in_put = f.readline().rstrip("\n").split()
    rsize = int(in_put[0])
    psize = int(in_put[1])
    count = 0
    direct = []
    for i in range(rsize):
        rowstring = f.readline()
        direct.append(splitString(rowstring))
    unsolved = []
    for j in range(psize):
        rowstring = f.readline()
        di = splitString(rowstring)
        unsolved.append(di)
        count += makeDirect(direct, di)
    #print k
    #print direct
    #print unsolved
    #print count
    string += "Case #" + str(k+1) + ": " + str(count) + "\n"


o = open('A-large-o.in', 'w')
o.write(string)
o.close()
