import sys

google = ("ejp mysljylc kd kxveddknmc re jsicpdrysi" +
          "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" +
          "de kr kd eoya kw aej tysr re ujdr lkgc jv")

english = ("our language is impossible to understand" +
           "there are twenty six factorial possibilities" +
           "so it is okay if you want to just give up")

google = google.replace(' ', '')
english = english.replace(' ', '')

translation = dict(zip(google, english))
translation['q'] = 'z'
translation['z'] = 'q'

def trans(ch, table):
    if ch in table:
        return table[ch]
    else:
        return ch

s = sys.stdin.readlines()[1:]

for i in range(len(s)):
    print 'Case #' + str(i+1) + ':',
    print ''.join(map(lambda x: trans(x, translation),
                      s[i].strip()))
