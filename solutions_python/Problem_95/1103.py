import string

from collections import defaultdict

mappings = {'ejp mysljylc kd kxveddknmc re jsicpdrysi':'our language is impossible to understand',
            'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
            'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up',
            'a zoo':'y qee'
           }

def default_value():
    return "Default Value"

googlerese = defaultdict(default_value)

missing_key = set(list(string.lowercase)) - set(list(" ".join(mappings.keys())))
missing_value = set(list(string.lowercase)) - set(list(" ".join(mappings.values())))

missing_key = list(missing_key)[0]
missing_value = list(missing_value)[0]

googlerese[missing_key] = missing_value

for key, value in mappings.items():
    googlerese.update(dict(zip(list(key),list(value))))

translate_table = string.maketrans("".join(googlerese.keys()),"".join(googlerese.values()))

T = int(raw_input())

for tc in range(T):
    input_str = raw_input()
    print "Case #%d: %s" % (tc+1,input_str.translate(translate_table))
