import sys

decoded_string = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

coded_string = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"

decode_map = {}
for i in range(len(coded_string)):
    decode_map[coded_string[i]] = decoded_string[i]

decode_map['z'] = 'q'
decode_map['q'] = 'z'

in_file = open(sys.argv[1])
out_file = open(sys.argv[2], 'w')

n = int(in_file.readline())

for i in range(1, n+1):
    out_file.write("Case #%d: " % i)
    for l in in_file.readline():
        out_file.write(decode_map.get(l, l))
out_file.close()
