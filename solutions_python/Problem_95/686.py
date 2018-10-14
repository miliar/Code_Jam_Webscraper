old = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
new = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

trans = {}

for i in range(len(old)):
    trans[old[i]] = new[i]
    
#trans['a'] = 'y'
#trans['o'] = 'e'
trans['z'] = 'q'
trans['q'] = 'z'
#trans['q'] = 'k'

in_data = open('A-small-attempt0.in').readlines()
N=in_data[0]
in_data=in_data[1:]
res = open('result', 'w')
case_no = 0
for line in in_data:
    case_no += 1
    line = line.strip()
    out = ''
    for l in line:
        out += trans[l]
    res.write('Case #' + str(case_no) + ': ' + out + '\n')
    
res.close()

