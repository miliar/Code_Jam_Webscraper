#!/usr/bin/python

def main():
    line = raw_input()
    l, d, n = map(lambda x: int(x), line.split(' '))
    base = []
    case = []
    for i in range(d):
        base.append(raw_input())
        
    for i in range(n):
        case.append(raw_input())
        
    i = 0
    for c in case:
        i += 1
        alpha = []
        par = False
        char_tmp = []
        for ch in c:
            if ch == '(':
                par = True
            elif ch == ')':
                alpha.append(''.join(char_tmp))
                par = False
                char_tmp = []
            else:
                if par:
                    char_tmp.append(ch)
                else:
                    alpha.append(ch)
            
        count = 0        
        for b in base:
            flag = 0
            for j in range(len(b)):
                if b[j] in alpha[j]:
                    flag += 1
            if flag == len(b):
                count += 1
        print 'Case #%d: %d' % (i, count)

if __name__ == '__main__':
    main()