import sys

def build_mapping():
    alphabet = set(list("abcdefghijklmnopqrstuvwxyz"))
    s = [
        "ejp mysljylc kd kxveddknmc re jsicpdrysi", 
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv", 
    ]

    a = [
        "our language is impossible to understand",
        "there are twenty six factorial possibilities",
        "so it is okay if you want to just give up"
    ]

    mapping = {}
    for i, sentence in enumerate(s):
        for j, ch in enumerate(sentence):
            mapping[ch] = a[i][j]
    # Hint
    mapping['q'] = 'z'
    # Find missing (z)
    keys = mapping.keys()
    values = mapping.values()
    mapping[list(alphabet - set(keys))[0]] = list(alphabet - set(values))[0]
    return mapping

def translate(mapping, sentence):
    translation = []
    for ch in sentence:
        translation.append(mapping[ch])
    return "".join(translation)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        mapping = build_mapping()
        lines = map(str.strip, f.readlines())
        for i, line in enumerate(lines[1:]):
            print "Case #%s: %s" % (i + 1, translate(mapping, line))