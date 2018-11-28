def rl(f):
    return f.readline().strip()

def main():
    inp = open("A-large.in")
    out = open("A-large.out", "w")

    N = int(rl(inp))
    for i in range(1, N+1):
        line = rl(inp).split(" ")
        lst = zip(*[iter(line[1:])]*2)
        t = 0
        r = {'O': (1, 0), 'B': (1, 0)}
        for robot, button in lst:
            button = int(button)
            rb, rt = r[robot]
            diff = abs(rb - button)
            if diff == 0 or diff <= t - rt:
                t += 1
            else:
                t += diff - (t - rt) + 1
            
            r[robot] = (button, t)

        print >>out, "Case #%d: %d" % (i, t)

    inp.close()
    out.close()

if __name__ == "__main__":
    main()
