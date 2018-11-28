#GJAM
#inn.in
from sys import * 

def execute():
        input_name = argv[1]
        output_name = "out.txt"
        input_file = open(input_name)
        output_file = open(output_name, 'w')

        main(input_file, output_file)

        input_file.close()
        output_file.close()

def main(input_file, output):
        # main algorithm goes here
        T = int(next(input_file))
        for case in range(T):
                line = next(input_file).strip().split()
                K = int(line[1])
                def trans(c):
                    if c == '+':
                        return 0
                    elif c == '-':
                        return 1
                def flip(row, pos, K):
                    for i in range(pos, pos + K):
                        row[i] = (row[i] + 1) % 2

                row = [trans(x) for x in line[0]]
                count = 0
                for i in range(len(row) - K + 1): 
                    if row[i] == 1:
                        count = count + 1
                        flip(row, i, K)
                done = True
                for i in range(len(row) - K + 1, len(row)):
                    if row[i] == 1:
                        done = False
                        break

                if done:
                    output.write("Case #" + str(case + 1) + ": " + str(count) + "\n")
                else:
                    output.write("Case #" + str(case + 1) + ": IMPOSSIBLE\n")

        input_file.close()
        output.close()

execute()
