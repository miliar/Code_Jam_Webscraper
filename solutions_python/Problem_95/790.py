replace = {
   'a' : 'y',
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
   ' ' : ' ',
    }

c = int(raw_input())

for i in range(c):
    line = raw_input()
    print 'Case #' + str(i+1) + ': ',
    l = []
    for s in line:
        l.append(replace[s])
    print str(''.join(l))

