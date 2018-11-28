#!/usr/bin/python
import string
frm = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvq'
to = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upz'

for i in range(97, 97 + 26):
    if chr(i) not in frm:
        frm = frm + chr(i)
        break
for i in range(97, 97+26):
    if chr(i) not in to:
        to = to + chr(i)
        break

trans = string.maketrans(frm, to)
# print string.translate('q', trans)
# print string.translate('z', trans)

def main():
    with open('1.in', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            if i == 0:
                continue
            print ('Case #%d: ' + string.translate(line, trans)) % i

if __name__ == '__main__':
    main()
