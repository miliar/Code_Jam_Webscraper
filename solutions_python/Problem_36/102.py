import time

in_file = "C-large.in"
out_file = "C-large.out"
TXT = "welcome to code jam"

def start():
    f_in = file(in_file, "r")
    f_out = file(out_file, "w")    
    N = int(f_in.readline().strip())

    for i in xrange(N):        
        line = f_in.readline().strip()
        n = getCount(line)
        rslt = str(n)
        while len(rslt) < 4:
            rslt = "0" + rslt
        
        f_out.write("Case #" + str(i+1) + ": " + rslt + "\n")

    f_in.close()
    f_out.close()

def getCount(line):
    size = len(TXT)
    indexes = []
    last_ind = -1
    for i in xrange(size):
        ind = line.find(TXT[i], last_ind+1)
        if ind == -1:
            return 0

        last_ind = ind
        local = []
        while ind != -1:
            local.append(ind)
            ind = line.find(TXT[i], ind+1)
        indexes.append(local)

    return getCounting(indexes)

def getCounting(indexes):
    counts = []

    cnts = []
    for j in xrange(len(indexes[0])):
        cnts.append(1)

    counts.append(cnts)
    
    for i in xrange(1, len(indexes)):
        local1 = indexes[i]
        local2 = indexes[i-1]
        cnts = []
        for j in xrange(len(local1)):
            c = 0
            for k in xrange(len(local2)):
                if (local1[j] > local2[k]):
                    c = c +  counts[i-1][k]
                else:
                    break
            c = c%10000
            cnts.append(c)
        counts.append(cnts)

    cnts = counts[len(counts)-1]
    c = 0
    for i in xrange(len(cnts)):
        c = c+cnts[i]

    return c%10000    

def removeElements(lst, elm):
    s = len(lst)
    j = -1
    for i in xrange(s):
        if (lst[s-1-i] <= elm):
            j = i
            break

    if j != 0:
        del lst[s-j:]
        
start()   
           
