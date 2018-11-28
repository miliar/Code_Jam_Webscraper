def is_palindrome(number):
    if number < 10:
        return True
    tmp = number
    a = []
    while tmp > 0:
        a.append(str(tmp%10))
        tmp = tmp/10
    if number==int("".join(a)):
        return True
    else:
        return False

filename = raw_input("Filename: ")
fh = open(filename, "r")
T = int(fh.readline())
out = open("out.txt", "w")
for counter in xrange(T):
    A, B = map(int, fh.readline().strip('\n').split(' '))
    fair_and_square = 0
    for counter2 in xrange(A, B+1):
        if int(counter2**0.5) == counter2**0.5:
            if is_palindrome(counter2) and is_palindrome(int(counter2**0.5)):
                fair_and_square += 1
    out.write("Case #%d: %d\n"%(counter+1, fair_and_square))
out.close()
