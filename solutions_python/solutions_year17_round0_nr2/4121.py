# cook your code here
t = input();
def areSorted(n):
    res = 0;
    p = 1
    next_digit = n%10;
    n = n/10;
    while (n):
        digit = n%10;
        if (digit > next_digit):
            digit = digit-1;
            res = (p*10-1);
        else:
            res = next_digit*p+res;
        next_digit = digit;
        n = n/10;
        p = p*10;
    res = next_digit*p+res
    return res;
for i in range(t):
    x = input();
    v = areSorted(x);
    print "Case #"+(str)(i+1)+": "+str(v);


