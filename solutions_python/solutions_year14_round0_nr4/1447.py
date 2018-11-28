#!/usr/bin python

#f = 'D-sample'
#f = 'D-small-attempt0'
f = 'D-large'

infile = f + '.in'
outfile = f + '.out'
output = []

with open(infile) as f:
    data = f.readlines()
    
num = int(data.pop(0))

def go_up(type):
    score[type] = score.get(type) + 1

for i in range(1, num + 1):

    nblocks = int(data.pop(0))
    decnaomi = map(float, data.pop(0).split())
    decken = map(float, data.pop(0).split())
    
    warnaomi = list(decnaomi)
    warken = list(decken)
    
    score = { 'deceit': 0, 'war': 0 }
    
    while len(warnaomi) > 0:
    
        # DECEITFUL
        # =========
        
        # choose block
        kenmax = max(decken)
        naomax = max(decnaomi)
        
        decken.remove(kenmax)
        
        if naomax < kenmax:
            decnaomi.remove(min(decnaomi))
        else:
            decnaomi.remove(min([v for v in decnaomi if v > kenmax]))
            go_up('deceit')
        
        # WAR
        # ===
        
        kenmax = max(warken)
        naomax = max(warnaomi)
        
        warnaomi.remove(naomax)
        
        if naomax > kenmax:
            warken.remove(min(warken))
            go_up('war')
        else:
            warken.remove(kenmax)
    
    output.append('Case #{}: {} {}'.format(
        i, score.get('deceit'), score.get('war')))

with open(outfile, 'w') as f:
    f.write('\n'.join(output))
