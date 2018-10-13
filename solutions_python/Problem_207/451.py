#--- READ INPUT ---#
inp = open('B-small-attempt0.in', 'r')
#inp = open('A-large.in', 'r')
#inp = open('test.in', 'r')
o = open('output.txt', 'w')
color_dict = {1:'R', 2:'O', 3:'Y',4:'G',5:'B',6:'V'}
test_cases = int(inp.readline())
for i in range(test_cases):
    line = inp.readline()[:-1].split(' ')
    cdic = {color_dict[j]:int(line[j]) for j in range(1, len(line))}
    n = int(line[0])
    '''
    r = int(line[1])
    o = int(line[2])
    y = int(line[3])
    g = int(line[4])
    b = int(line[5])
    v = int(line[6])
    '''
    possible = True if max(cdic.values()) < int(n/2 + 1) else False
    res = 'IMPOSSIBLE'
    if possible:
        rank = sorted(cdic, key=cdic.get, reverse=True)
        last = ''
        res = ''
        for j in range(n):
            if last != '':
                tmp = cdic[last]
                del cdic[last]
            m = max(cdic.values())
            max_colors = [x for x in cdic.keys() if cdic[x] == m]
            for k in rank:
                if k in max_colors:
                    next_color = k
                    break

            #next_color = max(cdic, key=cdic.get)
            res += next_color
            cdic[next_color] -= 1
            if last != '':
                cdic[last] = tmp
            last = next_color

    #--- WRITE OUTPUT ---#
    s = 'Case #' + str(i+1) + ': ' + res
    o.write(s + '\n')
inp.close()
o.close()
