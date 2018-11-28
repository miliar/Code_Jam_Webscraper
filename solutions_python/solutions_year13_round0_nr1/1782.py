def whowon(s):
    print s
    nodots = True
    for line in s:
        if '.' in line:
            nodots = False
        if allsame(line):
            if 'X' in line:
                return "X won"
            else:
                return "O won"
    if nodots:
        return "Draw"
    else:
        return "Game has not completed"

def allsame(s):
    if 'X' in s and ('.' not in s and 'O' not in s):
            return True
    if 'O' in s and ('.' not in s and 'X' not in s):
            return True
    return False      

def presmetajs(s1,s2,s3,s4):
    s5 = s1[0]+s2[0]+s3[0]+s4[0]
    s6 = s1[1]+s2[1]+s3[1]+s4[1]
    s7 = s1[2]+s2[2]+s3[2]+s4[2]
    s8 = s1[3]+s2[3]+s3[3]+s4[3]
    s9 = s1[0]+s2[1]+s3[2]+s4[3]
    s10 = s1[3]+s2[2]+s3[1]+s4[0]
    return whowon([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10])

f = open('./input', 'rU')
f2 = open('./output', 'w')
r = ''
for i in range(int(f.readline())):
    r+='Case #' + str(i+1) + ': ' + str(presmetajs(f.readline().strip('\n'),f.readline().strip('\n'),f.readline().strip('\n'),f.readline().strip('\n'))) + '\n'
    f.readline()
f2.write(r)
f.close()
f2.close()
