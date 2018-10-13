f = open('test4','r')
maxtests = int(f.readline())
testnum = 1
for line in f:
    si = line.split(' ')[1][:-1]

    def tillNext(si,begin):
        i = begin
        while i<len(si) and si[i] == '0':
            i += 1
        return i - begin

    toAdd = 0
    sums = 0
    for i in range(len(si)):
        num = si[i] 
        if sums <= i:
            t =  tillNext(si,i)
            toAdd += t
            sums += t
        sums += int(num)

    if testnum > maxtests:
        break
    print('Case #'+str(testnum) + ': '+ str(toAdd))

    testnum +=1

f.close()
