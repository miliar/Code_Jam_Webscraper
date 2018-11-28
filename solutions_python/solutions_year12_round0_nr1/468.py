mapping = {' ': ' ',
           'a': 'y',
           'b': 'h',
           'c': 'e',
           'd': 's',
           'e': 'o',
           'f': 'c',
           'g': 'v',
           'h': 'x',
           'i': 'd',
           'j': 'u',
           'k': 'i',
           'l': 'g',
           'm': 'l',
           'n': 'b',
           'o': 'k',
           'p': 'r',
           'q': 'z',
           'r': 't',
           's': 'n',
           't': 'w',
           'u': 'j',
           'v': 'p',
           'w': 'f',
           'x': 'm',
           'y': 'a',
           'z': 'q'}

f = file("A-small-attempt2.in",'r')
str1 = f.readlines()
substri = []
k = int(str1[0])
print k
for i in range(1,k+1) :
    str2=""
    for j in range(0,len(str1[i])-1) :
        str2+=mapping[str1[i][j]]
    substri.append(str2)
j = 1
for i in substri :
    print "Case #"+str(j)+": "+i
    j=j+1

