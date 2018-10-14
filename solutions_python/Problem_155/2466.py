T = input()

for n in range(T):
    Smax, Svalues = raw_input().split()
    Svalues = [int(x) for x in Svalues]
    to_be_invited = 0

    audience = 0

    for i,x in enumerate(Svalues):
        if audience < i:
            to_be_invited += (i-audience)
            audience += (i-audience) 
        audience += x

    print "Case #%d: %d" % (n+1, to_be_invited)



