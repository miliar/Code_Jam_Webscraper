import sys

fname = sys.argv[1]
file_in = open(fname,'r')
file_out = open(fname.replace(fname[fname.find('.')+1:],'out'),'w')

caseNum = 1
testCases = 0
currCase = caseNum


for l in file_in:
    l = l.strip()
    if testCases == 0:
        testCases = int(l)
        continue

    spl = l.split()
    # max shyness
    smax = int(spl[0])

    ppl = []
    pplCount = 0
    addition = 0
    written = False
    # all of the people with shyness given by idx
    for x,i in enumerate(spl[1]):
        ppl.append(int(x))

        if pplCount <  int(x) and int(i) > 0: # not enough ppl for x to clap
            # add enough ppl so that they will clap
            
            addition+=abs(int(x)-pplCount)


            pplCount +=abs(int(x)-pplCount)+int(i)
        elif pplCount >= int(x):
            pplCount += int(i)

        if pplCount >= smax:
            # got enough ppl for everyone to clap
            print l
            print 'Case #'+str(caseNum)+': ' +str(addition)
            file_out.write('Case #'+str(caseNum)+': ' +str(addition)+'\n')
            caseNum +=1
            written = True
            break

    if not written:
        print l
        print 'Case #'+str(caseNum)+': ' +str(addition)
        file_out.write('Case #'+str(caseNum)+': ' +str(addition)+'\n')
        caseNum+=1

file_in.close()
file_out.close()
