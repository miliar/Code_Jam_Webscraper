#-*-coding:utf-8-*-

import sys

def find(text, original, nt=0, no=0):
    n = 0
    c = original[no]
    for i in range(nt, len(text)):
        if text[i] == c:
            if no == len(original) - 1:
                n += 1
                pass
            else:
                n += find(text, original, i+1, no+1)
                pass
            pass
        pass
    return n
    
fh = open(sys.argv[1])
N = int(fh.readline())
for case_num in range(1, N+1):
    text = fh.readline()
    #print(text)
    n = find(text, 'welcome to code jam')
    print("Case #{0}: {1}".format(case_num, '0000{0}'.format(n)[-4:]))
    pass
