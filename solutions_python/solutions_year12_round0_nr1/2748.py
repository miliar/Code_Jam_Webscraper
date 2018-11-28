def is_numeric(lit):
    'Return value of numeric literal string or ValueError exception'
 
    # Handle '0'
    if lit == '0': return 0
    # Hex/Binary
    litneg = lit[1:] if lit[0] == '-' else lit
    if litneg[0] == '0':
        if litneg[1] in 'xX':
            return int(lit,16)
        elif litneg[1] in 'bB':
            return int(lit,2)
        else:
            try:
                return int(lit,8)
            except ValueError:
                pass
 
    # Int/Float/Complex
    try:
        return int(lit)
    except ValueError:
        pass
    try:
        return float(lit)
    except ValueError:
        pass
    return complex(lit)

def loadFile(filename):
    f = open(filename,'r')
    datalist = []
    for line in f:
        line=line.replace('\n','')
        linespaceless=line.replace(' ','')
        if linespaceless.isalpha():
            datalist.append(line)
        else:
            if line.isalnum():
                datalist.append(is_numeric(line))
            else:
                datalist.append([is_numeric(x) for x in line.split()])
    f.close()
    return datalist

def splitCases(data,noOfCases,linesPerCase):
    casechunks=[]
    for i in range(noOfCases):
        casechunks.append(data[1+i*linesPerCase:1+(i+1)*linesPerCase])
    return casechunks

def saveFile(val):
    f = open('output.txt','w')
    f.write(val)
    f.close()

def processCase(data):
    d = data[0]
    dd = ""
    replist1=['a',
              'b',
              'c',
              'd',
              'e',
              'f',
              'g',
              'h',
              'i',
              'j',
              'k',
              'l',
              'm',
              'n',
              'o',
              'p',
              'q',
              'r',
              's',
              't',
              'u',
              'v',
              'w',
              'x',
              'y',
              'z']
    replist2=['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
    for j in range(len(d)):
        if d[j] in replist2:
            dd=dd + replist1[replist2.index(d[j])]
        else:
            dd = dd + d[j]
    return dd

data = loadFile('A-small-attempt1.in')
dataCases = splitCases(data,data[0],1)

caseOutput = []
for case in dataCases:
    caseOutput.append(processCase(case))

totalstring = ""
for i in range(len(caseOutput)):
    totalstring = totalstring + "Case #"+str(i+1)+": "+caseOutput[i]+"\n"

print totalstring
saveFile(totalstring)
