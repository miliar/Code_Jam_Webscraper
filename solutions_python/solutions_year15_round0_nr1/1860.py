# standing ovation

infile = open("A-large.in",'rU')
out = open("ovation.out","w")

num_cases = int(infile.readline().strip())
for cur_case in range(1, num_cases + 1):
    line = infile.readline().strip().split()
    max_shy = int(line[0])
    array = [int(x) for x in line[1]]

    # compute stuff
    claps = 0
    extras = 0
    for x in range(max_shy + 1):
        if x <= claps:  # can add claps
            claps += array[x]
        else:  # need to insert members
            extras += x - claps 
            claps = x
            claps += array[x]
##            print("hi" + str(x))

    # output
    print("Case #{}: {}".format(cur_case, extras))
    out.write("Case #{}: {}\n".format(cur_case, extras))
    

infile.close()
out.close()
