def good(ss):
    if '-' in ss:
        return False

    return True

t = int(raw_input())
for i in range(t):
    dat = raw_input()
    ss, l = dat.split(' ')
    #print l
    l = int(l)
    ss = list(ss)

    num_flips = 0
    done = False
    for j in range(len(ss)-l+1):
        if good(ss):
            done = True
            break
        else:
            if ss[j] == '-':
                # Flip at point j if negative
                #print ss
                for k in range(l):
                    ss[j+k] = '+' if ss[j+k] == '-' else '-'

                #print "Flipped ",
                #print ss
    
                num_flips = num_flips + 1


    if good(ss):
        print "Case #" + str(i+1) + ": " + str(num_flips)
    else:
        print "Case #" + str(i+1) + ": IMPOSSIBLE"

    
