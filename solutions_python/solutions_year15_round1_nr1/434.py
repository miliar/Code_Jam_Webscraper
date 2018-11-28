if __name__=="__main__":
    file_in = open("A-large.in", "rt")
    file_out = open("A-large.out", "wt")

    T = int(file_in.next())
    for t in range(1, T + 1):
        N = int(file_in.next())
        M = map(int, file_in.next().split())

        y = 0
        rate = 0
        for n in range(1, N):
            diff = M[n] - M[n-1]
            if diff < 0:
                y += abs(diff)

                rate = max(rate, abs(diff))

        z = 0
        for n in range(N - 1):
            z += min(rate, M[n])





        file_out.write("Case #" + str(t) + ": " + str(y) + " " + str(z) + '\n')

    file_in.close()
    file_out.close()
