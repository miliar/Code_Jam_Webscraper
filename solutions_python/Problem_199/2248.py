t = int(input());

for i in range(0, t):
    s, p = input().strip().split(' ');
    s = [x for x in s.strip()];
    p = int(p);
    l = len(s);
    flips = 0;
    
    for j in range(0, l - p + 1):
        if s[j] == '-':
            flips = flips + 1;
            for k in range (j, j + p):
                if s[k] == '-':
                    s[k] = '+';
                else:
                    s[k] = '-';
                    
    if '-' in s[l - p:]:
        flips = "IMPOSSIBLE";
        
    print("Case #{}: {}".format(i + 1, flips));