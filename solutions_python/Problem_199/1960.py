
for T in range(1,int(raw_input()) + 1):
    ans = 0
    pancakes, flip = raw_input().split()
    flip = int(flip)
    pancakes = list(pancakes)
    
    if pancakes.count('-') > 0 and len(pancakes) - flip >= 0:
        i = pancakes.index('-')
        while i <= len(pancakes) - flip:
            for j in range(i, i + flip, 1):
                if pancakes[j] == '+':
                    pancakes[j] = '-'
                else:
                    pancakes[j] = '+'
            ans += 1
            if pancakes.count('-') > 0:
                i = pancakes.index('-')
            else:
                break
    
    if pancakes.count('-') == 0:
        print('Case #%d: %d'%(T, ans))
    else:
        print('Case #%d: IMPOSSIBLE'%(T))
    