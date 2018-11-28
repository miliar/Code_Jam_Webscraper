fin = open('A-small-attempt0.in', 'r')
fout = open('output.txt', 'w')
t = int(fin.readline())
dic = {'a' : 'y',
       'b' : 'h',
       'c' : 'e',
       'd' : 's',
       'e' : 'o',
       'f' : 'c',
       'g' : 'v',
       'h' : 'x',
       'i' : 'd',
       'j' : 'u',
       'k' : 'i',
       'l' : 'g',
       'm' : 'l',
       'n' : 'b',
       'o' : 'k',
       'p' : 'r',
       'q' : 'z',
       'r' : 't',
       's' : 'n',
       't' : 'w',
       'u' : 'j',
       'v' : 'p',
       'w' : 'f',
       'x' : 'm',
       'y' : 'a',
       'z' : 'q',
       ' ' : ' '
       }
for case in range(t):
    line = fin.readline().strip('\n')
    newline = ''
    for ch in line:
        newline = newline + dic[ch]
    fout.write('Case #{:d}: {:s}\n'.format(case+1, newline))
fin.close()
fout.close()
