def sol():
    def shorten(string):
        short = ''
        prevchar = ''
        l = []
        for char in string:
            if (char == prevchar):
                l[-1]+=1
            else:
                prevchar = char
                short += char
                l.append(1)
        return short, l

    global line_counter
    n = int(inp[line_counter])
    line_counter+=1
    ls = []
    short_form = None
    for i in range(n):
        _s,_l = shorten(inp[line_counter].strip())
        line_counter+=1
        if short_form == None:
            short_form = _s
            ls.append(_l)
        elif short_form == _s:
            ls.append(_l)
        else:
            return 'Fegla Won'
    TOTAL = 0
    #print ls
    for i in range(len(short_form)):
        _min = 999999
        for l1 in ls:
            total = 0
            for l2 in ls:
                total += abs(l1[i]-l2[i])
            if (total<_min):
                _min = total
        TOTAL += _min
    return str(TOTAL)

with open('A-small-attempt0 (1).in', 'r') as f:
#with open('LOL.txt', 'r') as f:
    inp = f.readlines()
    f.close()
line_counter = 0
T = int(inp[line_counter])
line_counter+=1
data = ''
for i in range(T):
    data += 'Case #%d:' %(i+1) + ' ' + sol()+'\n'
with open('output.txt', 'w') as f:
    f.write(data)
    f.close()
#print data
print 'done!'
