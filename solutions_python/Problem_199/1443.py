import sys

def flip(S, index, K):
    for i in range(index, index + K):
        if S[i] == '-':
            S[i] = '+'
        else:
            S[i] = '-'

def pancakes(input_file, output_file):
    T = int(input_file.readline())

    for case in xrange(1, T + 1):
        args = input_file.readline().split(' ')
        S = list(args[0])
        K = int(args[1])
        counter = 0
        flag = 0

        for index in range(len(S) - K + 1):
            if S[index] == '-':
                flip(S, index, K)
                counter = counter + 1
        for index in range(len(S) - K + 1, len(S)):
            if S[index] == '-':
                output_file.write("Case #" + str(case) + ": IMPOSSIBLE\n")
                flag = 1
                break
        if not flag:
            output_file.write("Case #" + str(case) + ": " + str(counter) + "\n")

input_file = open("C:\\Users\\doritm\\Desktop\\A-large.in", "r")
output_file = open("C:\\Users\\doritm\\Desktop\\output.out", "w")
pancakes(input_file, output_file)
input_file.close()
output_file.close()

