#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    fin = open("C-small-0.in", "r")
    fout = open("C-small-0.out", "w")
    T = int(fin.readline())

    mul = { ('1', '1'):'1', ('1', 'i'):'i', ('1', 'j'):'j', ('1', 'k'):'k',
            ('i', '1'):'i', ('i', 'i'):'-1', ('i', 'j'):'k', ('i', 'k'):'-j',
            ('j', '1'):'j', ('j', 'i'):'-k', ('j', 'j'):'-1', ('j', 'k'):'i',
            ('k', '1'):'k', ('k', 'i'):'j', ('k', 'j'):'-i', ('k', 'k'):'-1',
            ('-1', '1'):'-1', ('-1', 'i'):'-i', ('-1', 'j'):'-j', ('-1', 'k'):'-k',
            ('-i', '1'):'-i', ('-i', 'i'):'1', ('-i', 'j'):'-k', ('-i', 'k'):'j',
            ('-j', '1'):'-j', ('-j', 'i'):'k', ('-j', 'j'):'1', ('-j', 'k'):'-i',
            ('-k', '1'):'-k', ('-k', 'i'):'-j', ('-k', 'j'):'i', ('-k', 'k'):'1',
            ('1', '-1'):'-1', ('1', '-i'):'-i', ('1', '-j'):'-j', ('1', '-k'):'-k',
            ('i', '-1'):'-i', ('i', '-i'):'1', ('i', '-j'):'-k', ('i', '-k'):'j',
            ('j', '-1'):'-j', ('j', '-i'):'k', ('j', '-j'):'1', ('j', '-k'):'-i',
            ('k', '-1'):'-k', ('k', '-i'):'-j', ('k', '-j'):'i', ('k', '-k'):'1',
            }

    for t in xrange(0, T):
        L, X = tuple(map(int, fin.readline().strip().split()))
        pattern = list(fin.readline().strip())*X

        print "===========Case %d==============" % (t+1)

        answer = 'NO'

        if L > 1:
            left = 0
            right = L*X-1
            l_value = pattern[left]
            r_value = pattern[right]
            while True:
                while l_value != 'i' and left < right-2:
                    left += 1
                    l_value = mul[(l_value, pattern[left])]

                if l_value != 'i':
                    break

                while True:
                    while r_value != 'k' and right > left+2:
                        right -= 1
                        r_value = mul[(pattern[right], r_value)]

                    if r_value != 'k':
                        break

                    m_value = '1'
                    for m in xrange(left+1, right):
                        m_value = mul[(m_value, pattern[m])]

                    if m_value == 'j':
                        answer = 'YES'
                        break
                    else:
                        right -= 1
                        r_value = mul[(pattern[right], r_value)]

                if answer == 'YES':
                    break
                else:
                    left += 1
                    l_value = mul[(l_value, pattern[left])]

        fout.write("Case #%i: %s\n" % (t+1, answer))

    fin.close()
    fout.close()

