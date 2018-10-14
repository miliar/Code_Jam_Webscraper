for T in range(int(raw_input())):
    n = list(raw_input()[::-1]) +['0']
    l = len(n)-1
    lasst = -1
    for i in range(l):
        if(ord(n[i]) < ord(n[i+1])):
            n[i+1] = chr(ord(n[i+1])-1)
            lasst = i
    ans = int(''.join((n[::-1])[:l-lasst]+list('9'*(lasst+1))))
    print("Case #{}: {}".format(T+1,ans))