f = open('A-small-attempt1.in','r')
text = f.read()
text = text.replace('\r','')
lines = text.split('\n')

count = lines[0]
cases = lines[1:]

index = 0
caseIdx = 1

for i in xrange(10,len(cases)+1,10):
    case = cases[index:i]
    index += 10
    first = case[0]
    second = case[5]
    rowFirst = case[int(first)].strip()
    rowSecond = case[int(second)+5].strip()
    listFirst = rowFirst.split(' ')
    listSecond = rowSecond.split(' ')
    common = list((set(listFirst) & set(listSecond)))
    if len(common) == 1:
        print 'Case #'+str(caseIdx)+': '+common[0]
    elif len(common) == 0:
        print 'Case #'+str(caseIdx)+': Volunteer cheated!'
    else:
        print 'Case #'+str(caseIdx)+': Bad magician!'
    caseIdx += 1

    
