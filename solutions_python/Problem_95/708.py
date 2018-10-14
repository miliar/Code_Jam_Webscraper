s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
o1 = "our language is impossible to understand"
o2 = "there are twenty six factorial possibilities"
o3 = "so it is okay if you want to just give up"

s = s1 + s2 + s3
o = o1 + o2 + o3

letters = set([chr(l) for l in range(ord('a'), ord('z') + 1)])

mappings = dict(zip(s, o))

mappings['y'] = 'a'
mappings['e'] = 'o'
mappings['q'] = 'z'

missing_k = letters - set(mappings.keys())
missing_v = letters - set(mappings.values())

mappings[missing_k.pop()] = missing_v.pop();

with open("A-small-attempt0.in", "r") as infile:
    n_lines = int(infile.readline().strip())
    with open("output.txt", "w") as outfile:
        for i, line in enumerate(infile):
            i += 1
            if i <= n_lines:
                line = line.strip()
                output = "Case #%d: " % i
                for l in line:
                    output += mappings[l]
                outfile.write(output + "\n")

