#!/usr/bin/python
# Python 3.2.2

key_in = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''

key_out = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
'''

# create our key from the example
assert len (key_in) == len (key_out)
key = dict ()
for (kin, kout) in zip (key_in, key_out):
    if kin.isalpha ():
        assert kout.isalpha ()
        if kin in key:
            assert key[kin] == kout
        else:
            key[kin] = kout

# deduced form the hint
key['z'] = 'q'
key['q'] = 'z'

# did we get all the letters?
assert (ord ('z') - ord ('a'))

# now solve the problem
nr = int (input ())
for case_no in range (nr):
    to_translate = input ()
    result = list ()
    for c in to_translate:
        if c.isalpha ():
            result.append (key[c])
        else:
            result.append (c)
            
    result = ''.join (result)
    print ('Case #{}: {}'.format (case_no + 1, result))
