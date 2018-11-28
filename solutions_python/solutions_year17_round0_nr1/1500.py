def cal(x, sub):
    x = list(x)
    # find the first -
    p = 0
    flip = 0
    length = len(x)
    same = 0
    while p <= length-1 and same < length:

        if(x[p] == '-'):
            # flip the first S cakes
            # can we flip S pancakes?
            if (length - p) >= sub:
                # we can flip
                i = 0
                k = p
                flip += 1
                while (sub - i) > 0:
                    if x[k] == '-':
                        x[k] = '+'
                    else:
                        x[k] = '-'
                    i += 1
                    k += 1
                p = 0
            else:
                same = 10
                break

        else:
            if p <= length-1:
                p = p + 1
    return flip, same



def main():
    f = open('A-large.in', 'r')
    w = open('out.txt', 'w')
    i = 0
    for line in f:
        if i:
            line.strip()
            x = line.split(' ')
            ans = cal(x[0], int(x[1]))

            if(ans[1] > 1):
                res = "Case #"+str(i)+": "+'IMPOSSIBLE'
            else:
                res = "Case #" + str(i) + ": " + str(ans[0])
            w.write(res+'\n')
        i+=1
    f.close()
    w.close()

main()