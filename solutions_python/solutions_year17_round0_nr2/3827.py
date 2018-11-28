
for T in range(1, int(raw_input()) + 1):
    N = raw_input()
    
    found = False
    
    num = int(N) + 1
    while not found:
        num -= 1
        word = list(str(num))
        dec = False
        for i in range(len(word) - 1):
            if int(word[i]) > int(word[i + 1]):
                dec = True
        if not dec:
            found = True
    print('Case #%d: %d'%(T,num))