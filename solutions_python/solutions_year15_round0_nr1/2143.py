import sys

def main():
    f = None
    output = None
    case = 1
    if len(sys.argv) > 1 :
        f = open(sys.argv[1])
        output = open(sys.argv[1][:-2] + 'out', 'w')
    else:
        print("PROBLEM")
        return
    num_tests = int(f.readline().strip())
    for case in range(num_tests):
        output.write("Case #" + str(case+1) + ": ")
        line = f.readline().split()
        S0 = int(line[0])
        claps = 0
        friends = 0
        for i in range(S0+1):
            if claps < i:
                friends += (i - claps)
                claps = i
            claps += int(line[1][i])
        output.write(str(friends) + "\n")

    f.close()
    output.close()


if len(sys.argv) > 1:
    main()
