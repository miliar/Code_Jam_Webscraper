f = open('tidy.input')
line = f.readline()
num_test_cases = int(line)
completed_cases = 0
while completed_cases < num_test_cases:
    line = f.readline()
    line = str(line)
    tidy = False

    while (tidy == False):
        for i in range (0, len(line)):
            try:
                if int(line[i]) > int(line[i+1]):
                    line = str(int(line)-1)
                    break
            except:
                tidy = True


    print "Case #%i: %i" % (completed_cases + 1, int(line))
    completed_cases += 1
