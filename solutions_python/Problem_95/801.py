cypher_text = 'yeq ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
clear_text =  'aoz our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'


assert len(cypher_text) == len(clear_text)

key = {}

for a,b in zip(cypher_text, clear_text):
    if a in key:
        assert key[a] == b
    key[a] = b

alphabet = 'abcdefghijklmnopqrstuvwxyz'

missing_k = [a for a in alphabet if a not in key.keys()]
missing_v = [a for a in alphabet if a not in key.values()]

key[missing_k[0]] = missing_v[0]


base_name = 'A-small'
in_name = '{0}.in'.format(base_name)
out_name = '{0}.out'.format(base_name)

in_file = open(in_name)

test_count = int(in_file.readline())
lines = in_file.readlines()
lines = [line.strip() for line in lines]

out_file = open(out_name, 'w')

for i, line in enumerate(lines, 1):
    output = ''.join(key[c] for c in line)

    print('Case #{0}: {1}'.format(i, output))
    out_file.write('Case #{0}: {1}\n'.format(i, output))

out_file.close()