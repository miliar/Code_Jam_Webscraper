from math import pow

def is_tidy(num):
    idx = 0
    tidy = True
    while idx < len(num)-1:
        if num[idx] > num[idx+1]:
            return False
        idx += 1
    return True

def to_list(num):
    return [int(e) for e in str(num)]

def to_long(digits):
    return long(''.join([str(e) for e in digits]))

def tidy_up(digits):
    idx = len(digits)-1
    base = 0
    while idx > 0:
        if not is_tidy(digits):
            num = to_long(digits)
            num -= (digits[idx]+1) * int(pow(10, base))
            digits = to_list(num)
        else:
            break
        idx -= 1
        base += 1
    return digits

with open(r'D:\PycharmProjects\GCJ_2017\B-large.in', 'r') as inp:
    with open(r'D:\PycharmProjects\GCJ_2017\B-large.out', 'w') as outp:
        idx = 0
        nr_tc = 0
        for line in inp:
            if idx == 0:
                nr_tc = int(line.strip())
            else:
                digits = [int(e) for e in str(line.strip())]
                if is_tidy(digits):
                    tidy_number = ''.join([str(e) for e in digits])
                    print 'Case #%s: %s' % (idx, tidy_number)
                    outp.write('Case #%s: %s\n' % (idx, tidy_number))
                else:
                    tidy_number = ''.join([str(e) for e in tidy_up(digits)])
                    print 'Case #%s: %s' % (idx, tidy_number)
                    outp.write('Case #%s: %s\n' % (idx, tidy_number))
            #print idx
            idx += 1