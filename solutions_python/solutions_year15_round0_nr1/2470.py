def main():
    f1 = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    T = int(f1.readline().rstrip())
    for i in range(T):
        line = f1.readline().rstrip().split()
        n = int(line[0])
        sks = line[1]
        disp = []
        num = 0
        for j in range(n+1):
            disp.append(j-num)
            num += int(sks[j])
            friends = max(disp)
        f2.write("Case #" + str(i+1) + ": " + str(friends) + "\n")

main()
