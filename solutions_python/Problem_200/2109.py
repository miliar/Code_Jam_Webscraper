fin = open('tidy.in', 'r')
fout = open('tidy.out', 'w')

T = int(fin.readline().strip())

for t in range(T):
    N = list(fin.readline().strip())
    R = ""
    for i in range(len(N)):
        if i < len(N) - 1:
            if N[i] < N[i+1]:
                R = R + str(N[i])
            elif N[i] > N[i+1]:
                R = R + str(int(N[i]) - 1)
                for j in range(i + 1, len(N)):
                    R = R + '9'
                break
            else:
                j = i + 2
                while j < len(N):
                    if N[i] == N[j]:
                        j = j + 1
                    else:
                        break
                if j < len(N):
                    if N[i] < N[j]:
                        R = R + str(N[i])
                    else:
                        R = R + str(int(N[i]) - 1)
                        for j in range(i + 1, len(N)):
                            R = R + '9'
                        break
                else:
                    R = R + str(N[i])
        else:
            R = R + str(N[i])

    fout.write("Case #" + str(t+1) + ": " + str(int(R)) + "\n")

fin.close()
fout.close()
