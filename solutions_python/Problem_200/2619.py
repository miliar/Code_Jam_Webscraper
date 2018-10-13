# -*- coding: utf-8 -*-

# QR B.  Tidy Numbers
import itertools

#INPUT = 'B-small-attempt0.in'
#INPUT = 'qr_b-smaii.in'
#OUTPUT = 'qr_b-small.out'

INPUT = 'B-large.in'
OUTPUT = 'qr_b-large.out'


def result(caseno, msg):
    output = open(OUTPUT, 'a')
    output.write('Case #%d: %s\n' % (caseno, msg))
    output.close()

def createnumber(nlist):
    return int(''.join(nlist), 10)

def main():
    input = open(INPUT, 'r')

    case = int(input.readline().replace('\n',''))    # 1行目問題数
    
    for caseno in range(1, case+1):
        N = int(input.readline().replace('\n',''))

        if False:
            for i in reversed(range(1, N+1)):
                _i = [x for x in list(str(i))]

                if _i[0] > _i[len(_i)-1]:
                    continue

                _i.sort()
                j = createnumber(_i)
                if i == j:
                    result(caseno, j)
                    break

        if True:
            nlen = len(str(N))
            while True:
                comblist = list(itertools.combinations_with_replacement('123456789', nlen))
                if N < createnumber(comblist[0]):
                    nlen -= 1
                    continue

                for d in comblist[::-1]:
                    num = createnumber(d)
                    if num <= N:
                        result(caseno, num)
                        break

                break


if __name__ == '__main__':
    main()
