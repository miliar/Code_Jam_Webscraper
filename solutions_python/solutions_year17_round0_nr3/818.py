import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
lines = [x for x in lines if len(x) > 0]

T = int(lines[0],10)
for tt, l in enumerate(lines[1:]):
    N = int(l.split(" ")[0],10)
    K = int(l.split(" ")[1],10)        

    remaining = K

    # idea they will alternate sides always unless all spaces are 0,0
    # we can repeatedly split in half
    size_to_consider = N
    while 1:
        if remaining == 1:
            ans = (size_to_consider-1)/2, size_to_consider-1-(size_to_consider-1)/2
            break
        # now we split in 2 and take the correct side
        remaining -= 1
        side_sizes = (size_to_consider-1)/2, size_to_consider-1-(size_to_consider-1)/2
        if remaining % 2 == 0:
            size_to_consider = min(side_sizes)
            remaining = remaining/2
        else:
            size_to_consider = max(side_sizes)
            remaining = (remaining+1)/2

    print ("Case #%d:" % (tt+1)), ans[1], ans[0]

        

