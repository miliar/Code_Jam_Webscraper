from string import maketrans, whitespace, digits

def removeDuplicates(string):
    result=[]
    seen=set()
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)


intab = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvazq'
outtab = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upyqz'

trantab = maketrans(intab, outtab)

with open('a.in', 'r') as fin:
    with open('a.out', 'w') as fout:
        cases = int(fin.readline())
        for i in range(cases):
            googlerese = fin.readline()
            fout.write('Case #' + str(i+1) + ': ' + googlerese.translate(trantab));
            