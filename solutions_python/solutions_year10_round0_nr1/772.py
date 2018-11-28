nb_lines = int(raw_input())
for i in range(1, nb_lines + 1):
    line = raw_input()
    n = int(line.split(" ")[0])
    k = int(line.split(" ")[1])
    binary = bin(k)
    #print binary, binary[-n:], "1" * n
    if binary[-n:] == "1" * n:
        print "Case #" + str(i) + ": ON"
    else:
        print "Case #" + str(i) + ": OFF"
