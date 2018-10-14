#!/usr/bin/env python

def main():
    fin = open('B-large.in', 'r')
    fout = open('out.out', 'w')
    N = int(fin.readline().strip('\n'))
    for casenum in range(1, N+1):
        input = fin.readline().strip('\n').split()
        pos = 0
        combine = {}
        opposed = []
        if int(input[pos]) > 0:
            start = pos + 1
            end = start + int(input[pos])
            pos = end
            for x in range(start, end):
                a = input[x][0] + input[x][1]
                b = input[x][1] + input[x][0]
                c = input[x][2]
                combine[a] = c
                combine[b] = c
        else:
            pos += 1
        if int(input[pos]) > 0:
            start = pos + 1
            end = start + int(input[pos])
            pos = end
            for x in range(start, end):
                opposed.append(input[x][0] + input[x][1])
                opposed.append(input[x][1] + input[x][0])
        else:
            pos += 1
        numchars = input[pos]
        letters = input[pos+1]
        list = ''
        for letter in letters:
            list += letter
            if len(list) > 1:
                a = list[-2]
                b = list[-1]
                if a + b in combine:
                    list = list[:-2]
                    list += combine[a+b]
                elif b + a in combine:
                    list = list[:-2]
                    list += combine[b+a]
                for combo in opposed:
                    if combo[0] in list and combo[1] in list:
                        list = ''
        list2 = []
        for letter in list:
            list2.append(letter)
        list3 = '[' + ', '.join(list2) + ']'
        fout.write('Case #%d: %s\n' % (casenum, list3))
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()