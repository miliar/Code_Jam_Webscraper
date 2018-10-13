import sys

fd = open("./A-large.in", "r")

fout = open("./A-large.out", "w")

num_tests = int(fd.readline().strip())

for i in range(num_tests):
    test = fd.readline().strip().split(" ")

    s_max = int(test[0])
    digits = test[1]

    standing = 0
    friends = 0

    for j in range(s_max + 1):
        standing += int(digits[j])

        if standing <= j:
            friends += 1
            standing += 1


    fout.write("Case #{}: {}".format(i+1, friends)+"\n")
    print("Case #{}: {}".format(i+1, friends))


fout.close()
fd.close()
