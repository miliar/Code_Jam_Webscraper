in_1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
in_2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
in_3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
out_1 = "our language is impossible to understand"
out_2 = "there are twenty six factorial possibilities"
out_3 = "so it is okay if you want to just give up"

cache = {}
count = 0
while count < len(in_1):
    if not cache.has_key(in_1[count]):
        cache[in_1[count]] = out_1[count]
    count += 1
    
count = 0
while count < len(in_2):
    if not cache.has_key(in_2[count]):
        cache[in_2[count]] = out_2[count]
    count += 1
    
count = 0
while count < len(in_3):
    if not cache.has_key(in_3[count]):
        cache[in_3[count]] = out_3[count]
    count += 1


cache['z'] = 'q'
cache['q'] = 'z'

def get_out_string(inp):    
    outstr = []
    for x in inp:
       outstr.append(cache[x])
    return ''.join(outstr)

in_file = open('A-small-attempt0.in')
a = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
b = "our language is impossible to understand"

t = int(in_file.readline())
out_file = open('A-small-attempt0.txt','w')
for caseNo in xrange(1,t+1):    
    st = get_out_string(in_file.readline().strip(' \t\n\r'))
    out_file.write('Case #{0}: {1} \n'.format(caseNo, st))
