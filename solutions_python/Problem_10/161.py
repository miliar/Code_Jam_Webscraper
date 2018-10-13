f = open("A-large.in", "r")
num = int(f.readline())
count = 0
for i in xrange(num):
    count += 1
    stuff = f.readline()
    bits = stuff.split(' ')
    max_on_key = int(bits[0])
    num_keys = int(bits[1])
    num_letters = int(bits[2])
    t_letters = f.readline().split(' ')
    letters = []
    for l in t_letters:
        letters.append(int(l.strip()))
    letters.sort()

    total = 0
    cur = max_on_key
    mult = 1
    num = len(letters) - 1

    while num > -1:
        cur = num_keys
        while (cur > 0) and (num > -1):
            total += (letters[num] * mult)
            num -= 1
            cur -= 1
        mult += 1
    
    print "Case #" + str(count) + ": " + str(total)
    
