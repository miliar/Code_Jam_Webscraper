times = input()
loop = True

def toggle(element):
    return "+" if element == "-" else "-"


flip = 0

for i in range(1,times+1):
    loop = True
    flip = 0
    pancakes, pan_range = raw_input().split(' ')
    pancakes = list(pancakes)
    pan_range = int(pan_range)
    if len(set(pancakes)) == 1 and set(pancakes) == set(['+']):
        print("Case #{0}: {1}".format(i, flip))
    else:
        for idx1, pancake in enumerate(pancakes):
            if len(set(pancakes)) == 1 and set(pancakes) == set(['+']):
                print "Case #{0}: {1}".format(i, flip)
                break
        
            if pancake == "-":
                flip += 1
                for idx2 in range(pan_range):
                    try:
                        pancakes[idx1+idx2]
                    except IndexError:
                        loop = False
                        break
                    pancakes[idx1 + idx2] = toggle(pancakes[idx1+idx2])
        
            if loop == False:
                print "Case #{0}: {1}".format(i, "IMPOSSIBLE")
            	break
            
            else:
                continue

