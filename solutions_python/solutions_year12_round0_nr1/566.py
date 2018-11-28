a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq'
b = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz'

mapping = {}
for i in range(len(a)):
    mapping[a[i]] = ord(b[i]) - ord(a[i])

def translate(instr):
    theString = ""
    for j in range(len(instr)):
        theString += chr(ord(instr[j]) + mapping[instr[j]])
    return theString

fin = open('C:\\temp\\A-small-attempt0.in')
fout = open('C:\\temp\\file2.out','w')
cases = int(fin.readline())
for case in range(cases):
    fout.write('Case #' + str(case+1) + ': ' + translate(fin.readline().strip('"\n')) + '\n')