def translate(ch):
    if (ch == 'y'):
        return 'a'
    if (ch == 'n'):
        return 'b'
    if (ch == 'f'):
        return 'c'
    if (ch == 'i'):
        return 'd'
    if (ch == 'c'):
        return 'e'
    if (ch == 'w'):
        return 'f'
    if (ch == 'l'):
        return 'g'
    if (ch == 'b'):
        return 'h'
    if (ch == 'k'):
        return 'i'
    if (ch == 'u'):
        return 'j'
    if (ch == 'o'):
        return 'k'
    if (ch == 'm'):
        return 'l'
    if (ch == 'x'):
        return 'm'
    if (ch == 's'):
        return 'n'
    if (ch == 'e'):
        return 'o'
    if (ch == 'v'):
        return 'p'
    if (ch == 'z'):
        return 'q'
    if (ch == 'p'):
        return 'r'
    if (ch == 'd'):
        return 's'
    if (ch == 'r'):
        return 't'
    if (ch == 'j'):
        return 'u'
    if (ch == 'g'):
        return 'v'
    if (ch == 't'):
        return 'w'
    if (ch == 'h'):
        return 'x'
    if (ch == 'a'):
        return 'y'
    if (ch == 'q'):
        return 'z'
    if (ch == ' '):
        return ' '
    return ""
def convert_gg(s):
    output = ''
    for i in range(len(s)):
        output += translate(s[i])
    return output
        

f = open('C:\A-small-attempt0.in')
f_out = open('C:\\res.txt','r+')
j = 0
n = 0
for line in f:
    if (j == 0):
        n = int(line)
        j = j + 1
        continue
    f_out.write("Case #"+str(j)+": "+convert_gg(line)+'\n')
    j = j + 1

f.close()
f_out.close()

    
    
