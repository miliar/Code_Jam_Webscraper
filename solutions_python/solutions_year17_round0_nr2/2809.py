# Python 3.5

def main():
    problem = open("B-large.in", "r")
    output = open("B-out.txt", "w")

    test_case = int(problem.readline().strip())

    for test in range(test_case):
        N = list(problem.readline().strip())
        result = int(''.join(N))
        for idx in range(len(N)-1):
            if N[idx] > N[idx+1]:
                N[idx] = str(int(N[idx]) - 1)
                N[idx+1:] = ['9'] * (len(N)-(idx+1))
                for rev in range(idx-1, -1, -1):
                    if N[rev] > N[rev+1]:
                        N[rev] = str(int(N[rev]) - 1)
                        N[rev+1] = '9'
                result = int(''.join(N))
        output.write("Case #" + str(test+1) + ": ")
        output.write(str(result) + "\n")
    problem.close()
    output.close()

main()
    
