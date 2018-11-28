# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
#----------^

#----------v
output = None
if len(sys.argv) == 3:
    output = open(sys.argv[2], 'w')
input = open(sys.argv[1])
#----------^

#----------v
for n in range(int(input.readline())):
#----------^
    combos = []
    results = []
    opposed = []
    chunks = input.readline().split()
    for i in range(int(chunks.pop(0))):
        combo = chunks.pop(0)
        combos.append((combo[0], combo[1]))
        results.append(combo[2])
    for i in range(len(combos)):
        combos.append(combos[i][::-1])
        results.append(results[i])
    for i in range(int(chunks.pop(0))):
        opposed.append(tuple(chunks.pop(0)))
        opposed.append(tuple(opposed[-1][::-1]))
    spell = list(chunks[-1])
            
    res = []
    while spell != []:
        res.append(spell.pop(0))
        if len(res) > 1:
            try:
                i = combos.index((res[-1], res[-2]))
                if i != -1:
                    res.pop()
                    res[-1] = results[i]
            except:
                pass
            if len(res) == 1:
                continue
            for i in res[:-1]:
                if (i, res[-1]) in opposed:
                    res = []
                    break
    
    result = '['
    while res != []:
        result += res.pop(0)
        if res != []:
            result += ', '
    result += ']'
#----------v
    print("Case #"+str(n+1)+": "+str(result))
    if len(sys.argv) == 3:
        output.write("Case #"+str(n+1)+": "+str(result)+"\n")
if len(sys.argv) == 3:
    output.close()
#----------^










