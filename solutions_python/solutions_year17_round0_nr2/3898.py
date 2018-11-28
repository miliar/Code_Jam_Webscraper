n = int(raw_input());
for x in range(n):
    s =  map(int, list(raw_input()));
    l = len(s);
    i = l-1;
    while(i > 0):
        if(s[i] < s[i-1]):
            s[i-1] = s[i-1] -1; 
            j = i;
            while(j < l):
                s[j]= 9;
                j = j + 1;
        i = i -1;
    ans = map(str, s);
    ans =''.join(ans);
    print 'Case #'+str(x+1)+':',
    print int(ans);
