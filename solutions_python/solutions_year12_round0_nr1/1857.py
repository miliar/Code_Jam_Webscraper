__author__ = 'firefly'

map = dict()

sentences = ('ejp mysljylc kd kxveddknmc re jsicpdrysi'
             'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
             'de kr kd eoya kw aej tysr re ujdr lkgc jv'
             'yeq ')
trans = (
    'our language is impossible to understand'
    'there are twenty six factorial possibilities'
    'so it is okay if you want to just give up'
    'aoz ')


for i in range(len(sentences)):
    map[sentences[i]]= trans[i]

f = open('input','rt')

print(sorted((map.values())))
map['z']='q'

def translate(line):
    res = []
    for c in line.strip():
        res.append(map[c])
    return ''.join(res)

f.readline()
i=1
for line in f:
    print('Case #'+str(i)+': '+ translate(line))
    i+=1
