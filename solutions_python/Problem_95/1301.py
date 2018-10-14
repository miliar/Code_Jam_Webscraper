#Dylan Nelson
#Problem A
IFILE = 'A-small-attempt1.in'
OFILE = 'A-small-attempt1.out'
#=============================================================================

code = {}
keys = set([])
letters = list(' abcdefghijklmnopqrstuvwxyz')

def decode(s):
    o = ''
    for let in s:
        if let in keys : o += code[let]
        else:
            l = letters.pop(0)
            keys.add(let)
            code[let] = l
            o += l
    return o

def update(s, t):
    for i in range(len(s)):
        let = s[i]
        if not (let in keys):
            keys.add(let)
            code[let] = t[i]
            letters.remove(t[i])

def init():
    update('y qee', 'a zoo')
    update('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
    update('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
    update('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')


#=============================================================================
init()
fin = open(IFILE, 'r')
fout = open(OFILE, 'w')
T = int(fin.readline())
for i in range(1, T + 1):
    fout.write('Case #' + str(i) + ': ' + decode(fin.readline()[:-1]) + '\n')
fin.close()
fout.close()
