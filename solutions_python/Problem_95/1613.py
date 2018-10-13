def main():
##    key = '''
##    ejp mysljylc kd kxveddknmc re jsicpdrysi
##    rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
##    de kr kd eoya kw aej tysr re ujdr lkgc jv'''
##    pln = '''
##    our language is impossible to understand
##    there are twenty six factorial possibilities
##    so it is okay if you want to just give up'''
# sneaky sneaky hiding the q in tests...
    key2 = 'ynficwlbkuomxsevzpdrjgthaq'
    pln2 = 'abcdefghijklmnopqrstuvwxyz'
    table = str.maketrans(key2, pln2)

    strings = open(input(prompt='input')).readlines()
    strings = strings[1:]

    with open(input(prompt='output'), 'a') as outputFile:
        for i in range(len(strings)):
            s = 'Case #'+str(i+1)+': '+strings[i].translate(table)
            if i == len(strings) - 1:
                s = s.replace('\n','')
            outputFile.write(s)

if __name__ == '__main__':
    main()