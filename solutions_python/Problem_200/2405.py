t = int(input());

for i in range (0, t):
    n = [int(x) for x in input().strip()];
    
    l = len(n);
    j = l - 1;
    index9 = l;
    while j > 0:
        if n[j] < n[j - 1]:
            index9 = j;
            n[j - 1] = n[j - 1] - 1;
        j = j - 1;
    for k in range(index9, l):
        n[k] = 9;
    maxTidy = int(''.join(map(str, n)));
    print("Case #{}: {}".format(i + 1, maxTidy));
                    
                
