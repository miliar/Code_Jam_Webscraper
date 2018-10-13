from math import floor

f = open('in.txt', 'r')
out = open('out.out', 'w')

count = 0
for line in f:
    if count == 0:
		count += 1
		continue
    parts = line.split(' ')
    n = int(parts[0])
    k = int(parts[1])
    wc = [n]
    min_val = 0
    max_val = 0
    for p in range(0, k):
        ind = wc.index(max(wc))
        max_val = max(wc) / 2
        min_val = max_val - 1 if max(wc) % 2 == 0 else max_val 
        wc[ind] = max_val
        wc.insert(ind, min_val)

    out.write('Case #' + str(count) + ': ' + str(max_val) + ' ' + str(min_val) + '\n')
    count += 1

f.close()
out.close()
