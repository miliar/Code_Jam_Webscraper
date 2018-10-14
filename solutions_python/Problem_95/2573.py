result = []

mapping = {}
input  = "z q ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
output = "q z our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

for i,letter in enumerate(input):
    mapping[letter] = output[i]

with open('/Users/jspies/Downloads/A-small-attempt2.in', 'r') as f:
    for i, line in enumerate(f.readlines()):
        if not i == 0:
            result.append('Case #' + str(i) + ': ' + ''.join([mapping[l] for l in line[:-1]]))

with open('/Users/jspies/Downloads/A-small-attempt2.out', 'w') as f:
    f.write('\n'.join(result))
        
