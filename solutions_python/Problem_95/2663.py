def speakingintongues(string):
    list_strings = string.split()
    list_complete = []
    for elem in list_strings:
        list_letters = list(elem)
        list2 = []
        for el in list_letters:
            if el is 'y':
                list2.append('a')
            elif el is 'n':
                list2.append('b')
            elif el is 'f':
                list2.append('c')
            elif el is 'i':
                list2.append('d')
            elif el is 'c':
                list2.append('e')
            elif el is 'w':
                list2.append('f')
            elif el is 'l':
                list2.append('g')
            elif el is 'b':
                list2.append('h')
            elif el is 'k':
                list2.append('i')
            elif el is 'u':
                list2.append('j')
            elif el is 'o':
                list2.append('k')
            elif el is 'm':
                list2.append('l')
            elif el is 'x':
                list2.append('m')
            elif el is 's':
                list2.append('n')
            elif el is 'e':
                list2.append('o')
            elif el is 'v':
                list2.append('p')
            elif el is 'z':
                list2.append('q')
            elif el is 'p':
                list2.append('r')
            elif el is 'd':
                list2.append('s')
            elif el is 'r':
                list2.append('t')
            elif el is 'j':
                list2.append('u')
            elif el is 'g':
                list2.append('v')
            elif el is 't':
                list2.append('w')
            elif el is 'h':
                list2.append('x')
            elif el is 'a':
                list2.append('y')
            elif el is 'q':
                list2.append('z')
        list2 = "".join(list2)
        list_complete.append(list2)
    list_complete = " ".join(list_complete)
    return list_complete
        
            
fd = open("A-small-attempt3.in", 'r')
fd2 = open("A-small-attempt3.out", 'w+')
number = fd.readline()
number = int(number)
for i in range(number):
    string = fd.readline()
    fd2.writelines("Case #%d: %s\n" % ((i+1),speakingintongues(string)))
