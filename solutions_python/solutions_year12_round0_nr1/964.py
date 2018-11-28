#   Input
#   ejp mysljylc kd kxveddknmc re jsicpdrysi
#   rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#   de kr kd eoya kw aej tysr re ujdr lkgc jv
#
#
#   Output
#   Case #1: our language is impossible to understand
#   Case #2: there are twenty six factorial possibilities
#   Case #3: so it is okay if you want to just give up

d_in = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz'
d_out ='our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq'

d = {i:o for i,o in zip(d_in,d_out)}
d['\n'] = '\n'

#   li = ''.join(d[c] for c in d_in)
#
#   print li

myFile = open("A-small-attempt0.in", "r")
inputlist = list()
for myLine in myFile:
    if not inputlist:
        inputlist.append(int(myLine))
    else:
        inputlist.append(myLine)
myFile.close()

outputFile = open('speaktongues.out','w')
for casenum, line in enumerate(inputlist[1:]):
    outputFile.write('Case #'+str(casenum+1)+': '+''.join([d[letter] for letter in line]))

outputFile.close()

