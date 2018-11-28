import os

for f in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if f.endswith(".in"):
        f_in = open(f)
        f_out = open(f[:-3] + '.out', 'w')

date = f_in.read().split('\n')

out = ''

cases = date.pop(0)

counter = 1

for case in date:
    if not case:
        continue
    res = ''
    he1 = case.split(' ')
    he2 = map(int, list(he1[1]))
    res = 0
    for entry in range(0,len(he2)):
        if(entry == 0):
            continue
        diff = entry - sum(he2[0:(entry)])
        if(diff>0):
            he2[0] += diff
            res += diff

    out = out + 'Case #' + str(counter) + ': ' + str(res) + '\n'
    counter += 1

f_out.write(out)
f_out.close()
f_in.close()