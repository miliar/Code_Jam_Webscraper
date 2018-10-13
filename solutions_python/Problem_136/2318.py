#!env python

in_f = open('input', 'r')
in_lines = in_f.readlines()
num_cases = int(in_lines[0].strip())

for i in range(1, num_cases + 1):
    r = 2.0
    [c, f, x] = [float(x) for x in in_lines[i].strip().split(' ')]
    t = 0.0
    if x < c:
        t = x / r
    else:
        while True:
            time_to_win = t + (x / r)
            time_to_win_with_new_farm = t + (c / r) + (x / (r+f))
            if time_to_win_with_new_farm < time_to_win:
                t += c / r
                r += f
                continue
            else:
                t += x / r
                break
    print "Case #%d: %.7f" % (i, t)
