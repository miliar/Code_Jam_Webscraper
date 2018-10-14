for i,l in enumerate(open("downloads/A-large.in").readlines()[1:]):
    num_clapping = 0
    num_invited = 0
    for min,num in enumerate(l.split()[1]):
        if num_clapping < min:
            num_invited += (min - num_clapping)
            num_clapping += (int(num) + min - num_clapping)
        else:
            num_clapping += int(num)
    print "Case #%s: %s" % (i+1,num_invited)

