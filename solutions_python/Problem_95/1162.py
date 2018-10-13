fob = open("c:/inputs/codejam/A-small-practice.in",'r')
fob2 = open("c:/inputs/codejam/A-small-practice.out",'w')
numTest = int(fob.readline())
hint = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
hint2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
i=0
form = "Case #%s: "
key = {}
while(i<len(hint)):
    if key.has_key(hint[i]) == False:
        key[hint[i]] = hint2[i]
    i = i + 1
key['q'] = 'z'
key['z'] = 'q'
i = 0
while i < numTest:
    string = fob.readline()
    fob2.write(form % (str(i+1)))
    for char in string:
        if char == '\n':
            fob2.write('\n')
        else:
            fob2.write(key[char])
    i = i + 1
fob.close()
fob2.close()
