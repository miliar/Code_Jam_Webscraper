t = int(raw_input())

def separate(n):
    n = str(n)
    separation_index = 1;
    previous = n[0]
    for i in range(1,len(n)):
        if n[i]<previous:
            break
        else:
            separation_index += 1
            previous = n[i]
    return n[:separation_index], n[separation_index:]

def fix(a):
    reva = a[::-1]
    prev = reva[0]
    cnt = 0
    for i in range(1,len(reva)):
        if prev != reva[i]:
            break
        else:
            cnt += 1
    return reva[cnt:][::-1], cnt

for i in range(t):
    n = str(raw_input())
    p1, p2 = separate(n)
    if len(p1)==len(n):
        res = p1
    else: 
        p1, p2_fix_parameter = fix(p1)
        p2 += '9'*p2_fix_parameter
        res = str(int(p1)-1)+'9'*len(p2)
    print "Case #{}: {}".format(i+1, int(res))