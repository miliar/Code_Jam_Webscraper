file = open("cookie_test_sample.txt")
out = open('cookie_test.txt', 'w')
T = int(file.readline().strip())
case = 1
for cases in range(T):
    variables = file.readline().split()
    c = float(variables[0])
    f = float(variables[1])
    x = float(variables[2])
    cps = 2.0  # cookies per second
    seconds = []
    if c/cps + c/f == x/cps:
        seconds.append(x/cps)
    while c/cps + c/f < x/cps:
        seconds.append(c/cps)
        cps += f
    if c/cps + c/f > x/cps:
        seconds.append(x/cps)
    out.write("Case #%i: %.7f\n" % (case, sum(seconds)))
    case += 1
