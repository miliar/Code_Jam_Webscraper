def eat(mushrooms):
    min1 = 0
    max_rate = 0
    for i in range(len(mushrooms) - 1):
        rate = mushrooms[i] - mushrooms[i + 1]
        min1 += max(0, rate)
        max_rate = max(rate, max_rate)
    
    min2 = 0
    for i in range(len(mushrooms) - 1):
        rate = mushrooms[i] - mushrooms[i + 1]
        if mushrooms[i + 1] == 0: min2 += rate
        else: min2 += min(max_rate, mushrooms[i])
    
    return (min1, min2)
        
if __name__ == '__main__':
    for T in range(int(raw_input())):
        intervals = int(raw_input())
        mushrooms = [int(p) for p in raw_input().split(' ')]
        (min1, min2) = eat(mushrooms)
        print "Case #%d: %d %d" % (T+1, min1, min2)