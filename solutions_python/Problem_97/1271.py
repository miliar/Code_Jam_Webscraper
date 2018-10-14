# Solution for Google Code Jam 2012 Problem C

Cfile = open('C-small-attempt0.in', 'r')
T = int(Cfile.readline())
Data = [[int(x) for x in line.split()] for line in Cfile]
Cfile.close()
print Data
print T
Results = [0] * T

#def int_to_list(i):
#    for (
#    return [int(x) for x in str(i).zfill(9)]

def list_to_int(l):
    return int("".join(str(x) for x in l))

def Recycle(num, v):
    if (v == 0):
        return[num]
    listnum = list(str(num))
    length = len(listnum)
    dummy = [0] * (length + v)
    i = 0
    j = length - v
    while (j < length):
        dummy[i] = listnum[j]
        i = i + 1
        j = j + 1
    j = 0
    while (i < length):
        dummy[i] = listnum[j]
        i = i + 1
        j = j + 1
    listnum = dummy[0:length]
    x = list_to_int(listnum)
    return[x]
    
def intlength(num):
    i = 1
    while (i < 8):
        if (num/(pow(10,i)) == 0):
            return i
        else:
            i = i + 1   
    
x = 1234
print int(Recycle(x,1)[0])
print int(Recycle(x,2)[0])
print int(Recycle(x,3)[0])

print T

c = 0 #counter
low = 0 #lower limit
high = 0 #upper limit
k = 0 #inner counter
ilen = 0 #int length
j = 0 #ultrainner counter
kreclen = 0 #length of krec- initially ilen
fincount = 0 #final count of pairs


print intlength(43)
print intlength(432)
print intlength(32343)
print intlength(2000000)

while (c < T):
    low = Data[c][0]
    high = Data[c][1]
    k = low
    fincount = 0
    while (k < high):
        ilen = intlength(k)
        krecycle = [0] * ilen
        krecycle[0] = k
        j = 1
        while (j < ilen):
            krecycle[j] = Recycle(k, j)[0]
            j = j+1
        j = 1
        kreclen = ilen
        while (j < kreclen):
            if (not (k < krecycle[j] <= high)):
                del krecycle[j]
                kreclen = kreclen - 1
            else:
                j = j + 1
        kreclen = kreclen - 1
        fincount = fincount + kreclen
        k = k + 1
    Results[c] = fincount
    c = c + 1   

print Results

c = 0

RFile = open("C-small-result.txt", 'w')

while (c < T):
    RFile.write("Case #%d: %d\n" %(c+1,Results[c]))
    c = c + 1

                
