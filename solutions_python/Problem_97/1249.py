filein = open('C-small-attempt0.in')
fileout = open('output3.txt', 'w')

#class RecycledNum:
#    def __init__(self, pvalue):
#        self.value = pvalue
#        self.pair = []
#        self.size = findSize()
#        Update()
#
#        
#    def findSize(self):
#        temp = str(self.value)
#        return len(temp)

a = filein.readlines()
b = len(a)
for n in range(1,b):
    count = 0
    tempStr = ''
    tempStr += 'Case #%d: ' %(n)
    c = str(a[n]).split()
    size = len(c[0])
    if size == 1:
        tempStr += str(count)
        fileout.write(tempStr)
        fileout.write('\n')
        continue
    Min = int(c[0])
    Max = int(c[1])
    #if Min == Max:
    #    tempStr == str(count)
    #    fileout.write(tempStr)
    #    fileout.write('\n')
    #    continue
    i = Min
    while i < Max+1:
        temp = str(i)
        if temp[-1] == 0:
            i+=1
            continue
        if size == 2:
            if int(temp[1]) <= int(temp[0]):
                i += 1
                continue
            i1 = int(temp[1] + temp[0])
            if i1 > Max:
                i += 10 - int(temp[1]) + int(temp[0]) + 2
                continue
            if i1 > i and i1 <= Max:
                count += 1
                i+=1
                continue
            i+=1
            continue
        if size == 3:
            i1 = int(temp[-1:] + temp[:2])
            i2 = int(temp[-2:] + temp[:1])
            if i1 > i and i1 <= Max:
                count += 1
            if i2 > i and i2 <= Max:
                count += 1
            i+=1
            continue
        if size == 4:
            i1 = int(temp[-1:] + temp[:3])
            i2 = int(temp[-2:] + temp[:2])
            i3 = int(temp[-3:] + temp[:1])
            if i1 > i and i1 <= Max:
                count += 1
            if i2 > i and i2 <= Max:
                count += 1
            if i3 > i and i2 <= Max:
                count += 1
            i+=1
            continue
            
        i+=1
        
    tempStr += str(count)
    fileout.write(tempStr)
    fileout.write('\n')
    continue
    


#tempStr = ''
#tempStr += 'Case #%d: ' %(c)

filein.close()
fileout.close()
