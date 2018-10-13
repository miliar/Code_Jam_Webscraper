#!/usr/bin python
infile = 'A-small-attempt0.in'

res = "Case #{}: {}"
opts = {
    'cheat': "Volunteer cheated!",
    'bad': "Bad magician!"
    }

outdata = []

with file(infile) as f:
    indata = map(str.strip, f.readlines())

num = int(indata[0])

for n in range(1, num+1):
    step = (n-1)*9
    
    # ans 1
    ans = indata[n + step]
    # table 1
    table = {
        "1": indata[n + step + 1],
        "2": indata[n + step + 2],
        "3": indata[n + step + 3],
        "4": indata[n + step + 4]
        }
    
    p1 = table[ans].split()
    
    # ans 2
    ans = indata[n + 5 + step]
    # table 2
    table = {
        "1": indata[n + 5 + step + 1],
        "2": indata[n + 5 + step + 2],
        "3": indata[n + 5 + step + 3],
        "4": indata[n + 5 + step + 4]
        }
    p2 = table[ans].split()
    
    card = set(p1) & set(p2)
    
    if len(card) > 1:
        outdata.append(res.format(n, opts['bad']))
    elif len(card) < 1:
        outdata.append(res.format(n, opts['cheat']))
    else:
        outdata.append(res.format(n, card.pop()))


with file('A-small-attempt0.out', 'w') as f:
    f.write('\n'.join(outdata))
