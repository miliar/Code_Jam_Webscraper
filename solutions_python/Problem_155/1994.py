import string

def solve(data, n):
    data = string.strip(data)
    (s, slist) = data.split(" ")

    clap = 0
    friends = 0

    for i in range(len(slist)):

        if clap < i:
            friends += (i - clap)
            clap += (i - clap) + int(slist[i])
        else:
            clap += int(slist[i])

    print "Case #%d: %d" % (n, friends)

def start():
    N = 0
    n = 1

    for l in file('input.in'):
        if N == 0:
            N = int(l)
            continue
        
        solve(l, n)
        n += 1

start()
