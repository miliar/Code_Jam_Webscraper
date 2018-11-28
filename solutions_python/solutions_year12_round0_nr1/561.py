import sys

sample_input = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

sample_output = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

if __name__ == "__main__":

    mapping = { "y": "a", "e": "o", "q": "z" }
    mapping.update({ k: v for k, v in zip(sample_input, sample_output) 
                     if ord(k) >= ord('a') and ord(k) <= ord('z') })

    if len(mapping) == 25:
        chars = set(chr(c) for c in range(ord('a'), ord('z') + 1))
        last_key = chars - set(mapping.keys())
        last_value = chars - set(mapping.values())
        mapping[list(last_key)[0]] = list(last_value)[0]
    elif len(mapping) < 26:
        print("ERROR: Only have %d mappings" % len(mapping))
        sys.exit(1)

    T = int(sys.stdin.readline())
   
    for X in range(1, T+1):
        G = sys.stdin.readline().strip()
        S = ''.join(mapping.get(c, c) for c in G)
        print("Case #%d: %s" % (X, S)) 
