#Henry Maltby
#Code Jam 2017

def how_long(pos, dest, speed):
    """Returns the time it takes to move from pos to dest at speed."""
    return (dest - pos) / speed

def cruise_control(horses, dest):
    """
    Returns the time it takes to make it to the dest while matching speed
    with the slowest horse.
    """
    time = 0
    for h in horses:
        time = max(time, how_long(h[0], dest, h[1]))
    return dest / time


def A():
    """
    Runs the problem as dictated in problem spec.
    """
    f = open('A-large.in')
    g = open('A-large.out', 'w')

    T = int(f.readline())
    for i in range(T):
        D, N = [int(x) for x in f.readline().strip().split(' ')]
        K = []
        for j in range(N):
            K.append([int(x) for x in f.readline().strip().split(' ')])
        ans = cruise_control(K, D)
        g.write("Case #" + str(i + 1) + ": " + "{0:6f}".format(ans))
        if i != T - 1:
            g.write("\n")

A()
