#d = {
#        'ejp mysljylc kd kxveddknmc re jsicpdrysi': 'our language is impossible to understand',
#        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
#        'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up'
#        }
#
#mapping = {}
#
#for crypto_text, clear_text in d.iteritems():
#    for index, crypto_char in enumerate(crypto_text):
#        clear_char = clear_text[index]
#        if crypto_char not in mapping:
#            mapping[crypto_char] = clear_char
#        else:
#            if mapping[crypto_char] != clear_char:
#                print "WTF"
#
#mapping['z'] = 'q'

mapping = {' ': ' ',
           'a': 'y',
           'c': 'e',
           'b': 'h',
           'e': 'o',
           'd': 's',
           'g': 'v',
           'f': 'c',
           'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

def process(s):
    l = []
    for char in s:
        l.append(mapping[char])

    return ''.join(l)

number_of_cases = int(raw_input())
for case_number in xrange(1, number_of_cases+1):
    s = raw_input()

    result = process(s)

    print "Case #%d: %s" % (case_number, result)
    case_number += 1