__author__ = 'muhammadkhadafi'


def total_clappers(audiences):
    clappers = 0
    non_clapper = -1
    for i in range(0, len(audiences)):
        if clappers >= i:
            clappers += audiences[i]
        else:
            if audiences[i] != 0:
                non_clapper = i
                break
    return clappers, non_clapper


def get_additional_clapper(audiences):
    additional_clapper = 0
    while True:
        total_audience = sum(audiences)
        result = total_clappers(audiences)
        if result[0] == total_audience:
            break
        else:
            additional_clapper += (result[1] - result[0])
            audiences[0] += (result[1] - result[0])
    return additional_clapper


f_in = open('A-large.in', 'r')
f_out = open('outputlarge.txt', 'w')
cases = int(f_in.readline().rsplit()[0])
for i in range(1, cases+1):
    case = f_in.readline().rsplit()
    audiences = []
    for j in range(0, int(case[0])+1):
        audiences.append(int(case[1][j]))

    # print "case #" + str(i) + ": " + str(get_additional_clapper(audiences))
    f_out.write("case #" + str(i) + ": " + str(get_additional_clapper(audiences)))
    if i < cases:
        f_out.write('\n')
f_in.close()
f_out.close()
