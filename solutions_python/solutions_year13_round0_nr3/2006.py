import os

palindrome_square = [1, 4, 9, 121, 484]
input_file = open(os.getcwd() + "/C.in", 'r')

T = input_file.readline()

for i in xrange(0,int(T)):
    print "Case #%d:" % (i+1),
    rng = input_file.readline().split(" ")
    count = 0
    for x in xrange(int(rng[0]), int(rng[1])+1):
        if x in palindrome_square:
            count += 1

    print count
