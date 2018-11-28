import math
def ring(r, n):
    return (2 * r + 4 * n + 1)


def rings(r, m):
    n = m - 1
    return (2 * r + 1) * (n + 1) + 2 * (n * (n + 1))


def compute(r, t, step=0.01):
    on = 0
    n = 1
    paint = 0
    while abs(t - paint) > 0.01 and abs(n-on) > 0.01:
        paint = rings(r, n)
        on = n
        n += 1.0*n*(t - paint)/paint*step
#         print t, paint, n
    n = math.ceil(n)
    return int(n-1) if rings(r, n) > t else int(n)
 
def read_input(path):
    f = open(path, "r")
    lines = f.readlines()
    f.close()
    return lines


def write_output(results, path):
    f = open(path, "w")
    body = ""
    for i, result in enumerate(results):
        body += "Case #%d: %s\n" % (i + 1, result)
    f.write(body)
    f.close()


def main():
    lines = read_input("/Users/Jo/Downloads/A-small-attempt0.in")
    result = []
    for line in lines[1:]:
        r, t = line.split()
        p = (compute(int(r), int(t)))
        print ">>>", p
        result.append(p)
    write_output(result, "/Users/Jo/Downloads/small.out")

if __name__ == "__main__":
    main()
