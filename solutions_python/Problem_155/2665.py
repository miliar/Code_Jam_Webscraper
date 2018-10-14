if __name__ == '__main__':
    f = open("input.txt", "r")  
    g = open("output.txt", "w")
    num_of_tests = int(f.readline())
    for test in range(num_of_tests):
        line = f.readline().split()
        n = int(line[0])
        data = map(int, line[1])
        m, s = 0, 0
        for i in range(n + 1):
            if data[i] != 0:
                m = max(m, i - s)
            s += data[i]
        g.write("Case #{0}: {1}\n".format(test + 1, m))
