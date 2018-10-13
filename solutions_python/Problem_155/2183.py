__author__ = 'Kirby'

if __name__ == "__main__":
    fr = open("A-large.in", "r")
    fw = open("so2.out", "w")

    T = int(fr.readline())

    for i in range(1, T+1):
        [Smax, S_vec] = fr.readline().split()
        Smax = int(Smax)
        S_vec = map(int, list(S_vec))

        # General Algorithm:
        #   Friends = 0
        #   Scan the list accumulating the number of people at each shyness level until 0 people are at a level.
        #   If the accumulator <= index, friends and accumulator += index - accumulator + 1. Continue scanning.

        friends = 0
        accumulator = 0
        for level in range(0, Smax+1):
            if S_vec[level] == 0 and accumulator <= level:
                incr = level - accumulator + 1
                friends += incr
                accumulator += incr
            else:
                accumulator += S_vec[level]

        fw.write("Case #{0}: {1}\n".format(i, friends))



