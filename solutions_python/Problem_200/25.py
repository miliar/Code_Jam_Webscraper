
def tidy_numbers_solve(N):
    if N[0] == '0':
        return '9' * (len(N) - 1)
    for i in range(len(N) - 1):
        if N[i + 1] < N[i]:
            adjustedN = N[:i]
            adjustedN += str(int(N[i]) - 1)
            adjustedN += '9' * (len(N) - i - 1)
            return tidy_numbers_solve(adjustedN)
    return N
         
def tidy_numbers_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    for i in range(1, T + 1):
        N = f.readline().split()[0]
        tidy_N = tidy_numbers_solve(N)
        
        output_f.write("Case #" + str(i) + ": " + tidy_N + "\n")
    return 1

tidy_numbers_main("B-large.in", "B-large.out")
