infile = open('in')
outfile = open('out','w')

from itertools import combinations
from copy import deepcopy
def flip(l, index):
    for i in l:
        i[index] = 1-i[index]

n = int(infile.readline())
for casecounter in range(n):
    outfile.write('Case #' + str(casecounter+1) + ': ')
    l = int(infile.readline())
    s = []
    for i in range(l):
        s.append(infile.readline().strip())
    let = []
    char = s[0][0]
    count = 0
    for i in range(len(s[0])):
        if s[0][i] == char:
            count += 1
        else:
            let.append((char,[count]))
            char = s[0][i]
            count = 1
    let.append((char,[count]))
    nope = False
    total = 0
    for word in s[1:]:
        char = word[0]
        count = 0
        index = 0
        for i in range(len(word)):
            if word[i] == char:
                count += 1
            else:
                if index >= len(let) or let[index][0] != char:
                    nope = True
                    break
                let[index][1].append(count)
                char = word[i]
                count = 1
                index += 1
        if nope or index != len(let)-1 or let[index][0] != char:
            nope = True
            break
        let[index][1].append(count)
        count = 0
    print(let)
    for char, counts in let:
        print(counts)
        avg = round(sum(counts)/len(counts))
        print(avg)
        total += sum([abs(i-avg) for i in counts])
        print(total)
    if nope:
        outfile.write('Fegla Won\n')
        print('Fegla Won')
    else:
        outfile.write(str(total)+'\n')
