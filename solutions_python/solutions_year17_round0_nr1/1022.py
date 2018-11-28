t=int(input())
for case in range(1,t+1):
    s,k=input().split(' ')
    k=int(k)
    s=s.replace('+','1')
    s=s.replace('-','0')
    l=len(s)
    s=int(s,2)
    target = int("1"*l,2)
    key = s ^ target
    key_str = "{0:{1}b}".format(key,l)
    count = 0
    for idx in range(0,1 + l - k):
        if key_str[idx] == '1':
            shift = int("1"*k,2) << (l - (k + idx))
            s ^= shift
            key ^= shift
            key_str = "{0:0{1}b}".format(key,l)
            count += 1
    if s == target:
        result = count
    else:
        result = "IMPOSSIBLE"
    print("Case #{}: {}".format(case, result))
        
