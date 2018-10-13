# Python 3.5

def main():
    problem = open("A-large.in", "r")
    output = open("A-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        D = int(line[0])
        N = int(line[1])
        max_time = 0
        for i in range(N):
            line = problem.readline().strip().split()
            time = (D - int(line[0]))/int(line[1])
            if time > max_time:
                max_time = time
        answer = D / max_time
        output.write("Case #" + str(test+1) + ": ")
        output.write(str(round(answer, 6)) + "\n")
    problem.close()
    output.close()

main()
