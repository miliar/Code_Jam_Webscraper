def factor(n, noduplicates = False):
    intn = int(n)
    factors = {}
    lastfactor = n
    i = 0

    # 1 is a special case
    if n == 1:
        return {1: 1}

    while 1:
        i += 1

        # avoid duplicates like {1: 3, 3: 1}
        if noduplicates and lastfactor <= i:
            break

        # stop when i is bigger than n
        if i > n:
            break

        if n % i == 0:
            factors[i] = n / i
            lastfactor = n / i

    return factors

def findharm(low, high, play_list):
    harm = "NO"
    for i in range(low, high):
        okay = True
        for note in play_list:
            if not i in factor(int(note)):
                if not int(note) in factor(i):
                    okay = False
                    break
        if okay:
            harm = i
            break
    return str(harm)

in_file = open('in')
out_file = open("out","w")
number_of_tests = int(in_file.readline())
for test_case in range(number_of_tests):
    test_string = in_file.readline()[:-1]
    test_list1 = test_string.split(" ")
    low = int(test_list1[1])
    high = int(test_list1[2]) + 1
    line_2 = in_file.readline()[:-1]
    note = line_2.split(" ")
    out_file.write("Case #" + str(test_case + 1) + ": " + str(findharm(low,high,note)) + "\n")
out_file.close()
in_file.close()
