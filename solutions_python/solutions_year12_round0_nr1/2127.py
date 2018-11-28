import string

ENCODED="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"
DECODED="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"

# mapping from Googlerese to 'normal'
mapping = { 'y' : 'a', 'e' : 'o', 'q' : 'z'}

for g, o in zip(ENCODED, DECODED):
    mapping[g] = o # it's easier to have spaces as well

# at this point one character is missing
abc = [chr(x) for x in xrange(ord('a'), ord('z') + 1) ]
missing_g = ''
for c in abc:
    if c not in mapping:
        missing_g = c
        break
missing_o = ''
for c in abc:
    if c not in mapping.values():
        missing_o = c
        break

mapping[missing_g] = missing_o # 'z' -> 'q'

def translate(line):
    return string.join([mapping[c] for c in line], '')

def main():
    tc = "A-small-attempt0"
    f = open("%s.in" % (tc))
    T = int(f.readline())

    outf = open("%s.out" % (tc), "w")
    for i in xrange(1, T + 1):
        outf.write("Case #%d: " % (i))
        outf.write(translate(f.readline().strip()))
        outf.write("\n")

if __name__ == '__main__':
    main()