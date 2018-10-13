import sys

samples = [("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand"),
           ("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"),
           ("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up")]

decode = {}

for encoded, decoded in samples:
    for enc_char, dec_char in zip(encoded, decoded):
        decode[enc_char] = dec_char

# everything but q and z is in the samples, and q is in the problem statement.
decode['z'] = 'q'

decoded_set = set(decode.values())



# what's the missing character?
for i in range(ord('a'), ord('z') + 1):
    if not chr(i) in decoded_set:
        decode['q'] = chr(i)

lines = list(sys.stdin)
i = 1
for line in lines[1:]:
    decoded_line = ''.join(map(lambda x: decode[x] if x in decode else '', line))
    print("Case #{}: {}".format(i, decoded_line))
    i += 1

