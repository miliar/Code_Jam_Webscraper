#! /usr/bin/python

if __name__ == "__main__":
    cases = int(raw_input())
    for i in range(cases):
        msg = raw_input()
        alphabet = {msg[0]:1}
        digits = []
        base = 2
        l = len(msg)
        zeroed = False
        for j in range(l):
            m = str(msg[j])
            if not m in alphabet:
                if not zeroed:
                    alphabet[m] = 0
                    zeroed = True
                else:
                    alphabet[m] = base
                    base = base + 1
            digits.append(alphabet[m])

        min_time = 0
        for j in range(l):
            min_time = min_time + base**(l-j-1)*digits[j]
        print 'Case #%d: %d' % (i+1, min_time)

