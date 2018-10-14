#Google Code Jam - Qualification Round 2015
#Problem A. Standing Ovation

def getResult(s):
    s = s.split(' ')[1]
    if len(s)==1:
        return '0'
    n = 0
    count = 0
    for i in range(len(s)-1):
        n += int(s[i])
        if n < i+1:
            m = i+1-n
            count += m
            n += m
            
    return str(count)

def standing_ovation():
    fo = open('A-large.in','r')
    fw = open('A-large.ou','w')
    case = int(fo.readline().strip('\n'))
    for i in range(1,case+1):
        r = getResult(fo.readline().strip('\n'))
        fw.write('Case #'+str(i)+': '+r+'\n')
    fo.close()
    fw.close()

if __name__ == '__main__':
    standing_ovation()
