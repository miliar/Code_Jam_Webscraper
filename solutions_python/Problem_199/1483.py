def problem1():
    f = open("A-large.in", "r")
    f2 = open("A-large.out", "w")
    line = f.readline()
    for i in range(1, int(line.strip())+1):
        s, numstr = f.readline().strip().split()
        num = int(numstr)
        s = list(s)
        counter = 0
        for index in range(0,len(s)-num):
            if s[index] == "-":
                counter += 1
                for index2 in range(index, index+num):
                    if s[index2] == "+":
                        s[index2] = "-"
                    else:
                        s[index2] = "+"
        final = ""
        for index in range(len(s)-num, len(s)):
            final += s[index]
        if final == num*"+":
            f2.write("Case #" + str(i) + ": " + str(counter) + "\n")
        elif final == num*"-":
            f2.write("Case #" + str(i) + ": " + str(counter+1) + "\n")
        else:
            f2.write("Case #" + str(i) + ": IMPOSSIBLE\n")
                    
    f.close()
    f2.close()


problem1()
