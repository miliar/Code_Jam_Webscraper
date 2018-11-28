import sys
import string

# should cover all possibilities except maybe 1, which we can figure out later
examples = {'ejp mysljylc kd kxveddknmc re jsicpdrysi': 'our language is impossible to understand',
            'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
            'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up',
            'y qee': 'a zoo'}

decode = {}
for k,v in examples.items():
    for i in range(len(k)):
        # including spaces makes it easier
        decode[k[i]] = v[i]
# figure out the MAX one that is unspecified
for let in string.lowercase:
    if let not in decode:
        unspec = let
        break
for let in string.lowercase:
    if let not in decode.values():
        ans = let
        break
decode[unspec] = ans

# after we have figured ot the alphabet
def translate(google):
    out = []
    for letter in google:
        out.append(decode[letter])
    return ''.join(out)

f = open('speaktongues-small.txt', 'w')
numTests = int(sys.stdin.readline())
lines = sys.stdin.readlines()
for i in range(1,numTests+1):
    google = lines[i-1].rstrip('\n')
    english = translate(google)
    f.write('Case #' + str(i) + ': ' + english + '\n')
f.close()