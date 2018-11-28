import io, string

# main
infile = open('A-small-attempt2.in', 'r')
times = infile.readline()
for case in range(int(times)):
    # read first arrangement
    ans1 = infile.readline()
    row1 = []
    for i in range(1,5):
        temp = infile.readline()
        if i == int(ans1):
            temp = temp.strip()
            row1 = temp.split(" ")
    # read second arrangement
    ans2 = infile.readline()
    row2 = []
    for j in range(1,5):
        tmp = infile.readline()
        if j == int(ans2):
            tmp = tmp.strip()
            row2 = tmp.split(" ")
    # compare results from arrangements
    res = list(set(row1).intersection(row2))
    # print results to user
    print("Case #%d: " % (case + 1),end="")
    if (len(res) == 0):
        print("Volunteer cheated!")
    elif (len(res) == 1):
        print("%s" % (res[0]))
    else:  # len(res) > 1
        print("Bad magician!")
infile.close()
