if __name__ == "__main__":
    t = int(raw_input())

    for i in range(1, t + 1):
        n, m = [s for s in raw_input().split(" ")]  
        if not '-' in n:
            print "Case #{}: {}".format(i, 0)
        else:
            count = 0
            for x in xrange(0, len(str(n))- int(m)+1):
                if n[x] == '-':
                    count += 1
                    n = n[:(x)] + '+' + n[(x+1):]                    
                    for char in xrange(x +1, x+ int(m)):
                        if n[char] == '-':
                            n = n[:(char)] + '+' + n[(char+1):]
                        elif n[char] == '+':
                            n = n[:(char)] + '-' + n[(char+1):]
                if '-' not in n: 
                    break

            if '-' in n[(len(str(n))- int(m)):]:
                    print "Case #{}: {}".format(i, "IMPOSSIBLE")
            else:
                   print "Case #{}: {}".format(i, count)

            