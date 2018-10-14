T = int(raw_input())

def toggle(str):
    for i in range(0, len(str)):
        if str[i] == '-':
            str = str[:i] + '+' + str[i+1:]
        else:
            str = str[:i] + '-' + str[i+1:]
    return str

assert(toggle('+++') == '---')
assert(toggle('+-+') == '-+-')
assert(toggle('+++---') == '---+++')

for i in range(1, T+1):
    print "Case #%d:" % i,

    pancakes, flipper = raw_input().split()
    flipper = int(flipper)

    pancakes_len = len(pancakes)
    
    if flipper > pancakes_len:
        print "impossible" if pancakes.find('-')>-1 else 0
        continue

    if flipper == 1:
        print  pancakes.count('-')
        continue
    solution = 0
    for e in range(0, pancakes_len-flipper+1):

        if e == pancakes_len-flipper:
            if pancakes.count('-') == flipper:
                print solution+1
                break
            if pancakes.count('-') == 0:
                print solution
                break
            if pancakes.count('-') < flipper:
                print "IMPOSSIBLE"
                break
        if pancakes[e] == '-':
            pancakes = pancakes[0:e] + toggle(pancakes[e:e+flipper]) + pancakes[e+flipper:]
            solution += 1
    
