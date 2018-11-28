


if __name__ == '__main__':
    #f = open("test.txt", "r")
    f = open("A-large.in", "r")
    test_num = int(f.readline())
    for i in range(1, test_num+1):
        L1 = f.readline().split(" ")
        if i != test_num:
            L1[1] = L1[1][:-1]
        max_level = int(L1[0])
        ppl_needed = 0
        ppl_standing = int(L1[1][0])
        for j in range(1, max_level+1):
            if ppl_standing < j:
                ppl_needed += j - ppl_standing
                ppl_standing = j
            ppl_standing += int(L1[1][j])
        print("Case #{0}: {1}".format(i, ppl_needed))