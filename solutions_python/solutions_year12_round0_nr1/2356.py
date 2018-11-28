samples = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', \
'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', \
'de kr kd eoya kw aej tysr re ujdr lkgc jv']

outs = ['our language is impossible to understand', \
'there are twenty six factorial possibilities', \
'so it is okay if you want to just give up']

map = {}
map['y'] = 'a'
map['e'] = 'o'
map['q'] = 'z'

for i in range(len(samples)):
    for j in range(len(samples[i])):
        if samples[i][j] not in map and samples[i][j]:
            map[samples[i][j]] = outs[i][j]
            
# print len(map)
# for item in map:
#     print item, map[item]

# For simplicity:
map['\n'] = ''
# By inspection:
map['z'] = 'q'

def map_string(s):
    res = ''
    for char in s:
        res += map[char]
    return res


if __name__ == "__main__":
    f = open('A-small-attempt0.in')
    num_test_cases = f.readline()
    c = 1
    
    output = open('A-small-output.txt', 'w')
    
    for line in f:
        x = "Case #{}: {}" .format(c, map_string(line))
        output.write(x + '\n')
        c += 1