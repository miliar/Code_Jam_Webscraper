print '1\n2\n3\n11'
a='11'
def is_pal(x):
    n = len(x)
    return x[:n/2][::-1] == x[(n+1)/2:]
while len(a)<=50:
    n = len(a)
    if n%2==0:
        if a[0]=='2': a = '1' + '0'*(n-1) + '1'
        elif a=='1'*n: a = '2' + '0'*(n-2) + '2'
        else:
            last = (n-1)/2
            while a[last]=='1': last-=1
            a = a[:last]+'1'+'0'*(n-2-2*last) + '1' + a[:last][::-1]
    else:
        if a[0]=='2':
            if a[n/2]=='0': a = a[:n/2]+'1'+a[n/2+1:]
            else: a = '1' + '0'*(n-1) + '1'
        elif a=='1'*(n/2)+'2'+'1'*(n/2): a = '2' + '0'*(n-2) + '2'
        elif a[n/2]=='0': a = a[:n/2]+'1'+a[n/2+1:]
        elif a[n/2]=='1': a = a[:n/2]+'2'+a[n/2+1:]
        else:
            last = n/2-1
            while a[last]=='1': last-=1
            a = a[:last]+'1'+'0'*(n-2*last-2)+'1'+a[:last][::-1]
    b = int(a)
    if is_pal(str(b**2)):
        print b
