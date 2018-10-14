#
#3
#ejp mysljylc kd kxveddknmc re jsicpdrysi
#rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#de kr kd eoya kw aej tysr re ujdr lkgc jv
#
#
#Output
#         ejp mysljylc kd kxveddknmc re jsicpdrysi
#Case #1: our language is impossible to understand
#         rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
#Case #2: there are twenty six factorial possibilities
#         de kr kd eoya kw aej tysr re ujdr lkgc jv
#Case #3: so it is okay if you want to just give up

f = open('input', 'r')
len = f.readline()
print len.rstrip()
i=0
for x in range(int(len)):
    i+=1
    line = f.readline()
    line = line.rstrip()
    nl = ''
    for x in line:
        if x == 'a': nl += 'y'
        elif x == 'b': nl += 'h'
        elif x == 'c': nl += 'e'
        elif x == 'd': nl += 's'
        elif x == 'e': nl += 'o'
        elif x == 'f': nl += 'c'
        elif x == 'g': nl += 'v'
        elif x == 'h': nl += 'x'
        elif x == 'i': nl += 'd'
        elif x == 'j': nl += 'u'
        elif x == 'k': nl += 'i'
        elif x == 'l': nl += 'g'
        elif x == 'm': nl += 'l'
        elif x == 'n': nl += 'b'
        elif x == 'o': nl += 'k'
        elif x == 'p': nl += 'r'
        elif x == 'q': nl += 'z'
        elif x == 'r': nl += 't'
        elif x == 's': nl += 'n'
        elif x == 't': nl += 'w'
        elif x == 'u': nl += 'j'
        elif x == 'v': nl += 'p'
        elif x == 'w': nl += 'f'
        elif x == 'x': nl += 'm'
        elif x == 'y': nl += 'a'##
        elif x == 'z': nl += 'q'
        else: nl +=x





    #print 'Case #'+str(i)+': '+line
    print 'Case #'+str(i)+': '+nl
