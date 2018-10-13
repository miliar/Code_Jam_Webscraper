#!/usr/bin/python

# Google Code Jam Qualification B

def tidyNumCheck(num):
    '''checks if number is tidy number'''
    assert type(num) == list
    return sorted(num) == num

def tidyNumGen(max_num):
    '''generates the new tidy number, recursively'''
    seq = list(str(max_num))
    for i in xrange(2, len(seq)+1):
        if not tidyNumCheck(seq[:i]):
            pad = ['0'] * (len(seq) - (i - 1))
            new_seq = seq[:i-1] + pad
            new_num = int(''.join(new_seq))
            return tidyNumGen(new_num - 1)
    return max_num # the number is already a tidy number

def main():
    t_val = input('')
    for n_idx in xrange(t_val):
        new_num = input('')
        answ = tidyNumGen(new_num)
        print 'Case #%d: %d' % (n_idx+1, answ)

if __name__ == '__main__':
    main()