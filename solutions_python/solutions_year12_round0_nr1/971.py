inf = open("A-small-attempt2.in", "r")
out = open("googlerese.txt", "w")
out.close()

numLp = int(inf.readline())

for i in range(0,numLp+1):
    mystring = inf.readline()
    orig = ""
    for char in mystring:
        if char == 'c':
            orig = orig + 'e';
        elif char == 'r':
            orig = orig + 't';
        elif char == 'y':
            orig = orig + 'a';
        elif char == 'e':
            orig = orig + 'o';
        elif char == 'k':
            orig = orig + 'i';
        elif char == 's':
            orig = orig + 'n';
        elif char == 'd':
            orig = orig + 's';
        elif char == 'b':
            orig = orig + 'h';
        elif char == 'p':
            orig = orig + 'r';
        elif char == 'i':
            orig = orig + 'd';
        elif char == 'm':
            orig = orig + 'l';
        elif char == 'f':
            orig = orig + 'c';
        elif char == 'j':
            orig = orig + 'u';
        elif char == 'x':
            orig = orig + 'm';
        elif char == 't':
            orig = orig + 'w';
        elif char == 'w':
            orig = orig + 'f';
        elif char == 'l':
            orig = orig + 'g';
        elif char == 'a':
            orig = orig + 'y';
        elif char == 'f':
            orig = orig + 'p';
        elif char == 'n':
            orig = orig + 'b';
        elif char == 'g':
            orig = orig + 'v';
        elif char == 'o':
            orig = orig + 'k';
        elif char == 'u':
            orig = orig + 'j';
        elif char == 'h':
            orig = orig + 'x';
        elif char == 'f':
            orig = orig + 'q';
        elif char == 'q':
            orig = orig + 'z';
        elif char == 'v':
            orig = orig + 'p';
        elif char == 'z':
            orig = orig + 'q';
        else:
            orig = orig + char;
    i = i + 1

    outf = open("Googlerese.txt", "a")
    outf.write("Case #" + str(i) + ": " + orig)
