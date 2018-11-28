def ord2(letter):
    return ord(letter)-ord('A')


def g(cnts, letter, S):
    n = cnts[ord2(letter)]
    for c in S:
        cnts[ord2(c)] -= n
    
    return n

def f(S):
    cnts = [0]*26

    for letter in S:
        cnts[ord2(letter)] += 1

    nums = [0]*10
    nums[0] = g(cnts, 'Z', 'ZERO')
    nums[2] = g(cnts, 'W', 'TWO')
    nums[4] = g(cnts, 'U', 'FOUR')
    nums[6] = g(cnts, 'X', 'SIX')
    nums[8] = g(cnts, 'G', 'EIGHT')
    # -----
    nums[3] = g(cnts, 'H', 'THREE')
    # -----
    nums[1] = g(cnts, 'O', 'ONE')
    # -----
    nums[7] = g(cnts, 'S', 'SEVEN')
    # -----
    nums[5] = g(cnts, 'V', 'FIVE')
    # -----
    nums[9] = g(cnts, 'E', 'NINE')

    dial = ''
    for i in range(10):
        dial += str(i)*nums[i]

    return dial


    
t = int(input())
for i in range(t):
    print('Case #' + str(i+1) + ':', f(input()))
