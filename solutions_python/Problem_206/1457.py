def calculate(km, n, lista):
    km = float(km)
    velocitats = []
    for horse in lista:
        hours = (km - horse[0])/horse[1]
        v = km / hours
        velocitats.append(v)
    return min(velocitats)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    km, n = raw_input().split()
    km, n = int(km), int(n)
    lista = []
    for j in range(n):
        k, s = raw_input().split()
        k, s = int(k), int(s)
        lista.append([k,s])

    r = calculate(km, n, lista)
    print "Case #{}: {} ".format(i, r)
    # check out .format's specification for more formatting options
