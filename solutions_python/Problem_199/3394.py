
ran = int(raw_input())
for T in range(1,ran + 1):
    ans = 0
    test = raw_input()
    test = test.split()
    spatula = int(test[1])
    sentence = list(test[0])
    
    if sentence.count('-') > 0 and len(sentence) - spatula >= 0:
        i = sentence.index('-')
        while i <= len(sentence) - spatula:
            for j in range(i, i + spatula):
                if sentence[j] == '+':
                    sentence[j] = '-'
                elif sentence[j] == '-':
                    sentence[j] = '+'
            ans += 1
            if sentence.count('-') > 0:
                i = sentence.index('-')
            else:
                break
    
    if sentence.count('-') == 0:
        print('Case #%d: %d'%(T, ans))
    else:
        print('Case #%d: IMPOSSIBLE'%(T))