def greatestcommondivisor(x,x1):
    if x1==0:
        return x
    else:
        return greatestcommondivisor(x1, x%x1)

testcases = int(raw_input())
counter = 1
impossible = False
while testcases > 0:
    inp = raw_input()
    fract = inp.split("/")
    divisor = greatestcommondivisor(int(fract[0]), int(fract[1]))
    fract[0] = ( float(fract[0])/float(divisor) )
    fract[1] = ( float(fract[1])/float(divisor) )
    a = float(fract[0]) / float(fract[1])
    if int(fract[1]) & int(fract[1])-1 != 0:
        impossible = True
    gen = 1
    while a * 2 < 1:
        a = a * 2
        gen += 1
    if impossible == True:
        print "Case #" + str(counter) + ": impossible"
    else:
        print "Case #" + str(counter) + ": " + str(gen)
    impossible = False
    testcases -= 1
    counter += 1
