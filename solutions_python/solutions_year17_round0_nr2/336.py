fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
T = int(fin.readline())
for cID in range(T):
    s = fin.readline()
    num = [int(x) for x in s.strip()]
    num = num[::-1]
    last = -1
    for i in range(len(num) - 1):
        if num[i] < num[i+1]:
            num[i] = 9
            num[i+1] -= 1
            last = i
    for i in range(last+1):
        num[i] = 9
    r = ''
    for c in num[:-1]:
        r = str(c) + r 
    if num[-1] != 0:
        r = str(num[-1]) + r  
    fout.write('Case #{}: {}\n'.format(cID+1, r))
