fin = file("B-large.in", "rU")
fout = file("B-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip()

    #print line

    num = [int(x) for x in list(line)] # treat as list

    #print num

    result = ''

    for j in xrange(1, len(num)):
        if num[j] < num[j-1]: # number went backwards
            decrease_index = j-1

            # should never be less than, but sanity check
            while decrease_index > 0 and num[decrease_index] <= num[decrease_index-1]:
                decrease_index -= 1

            if decrease_index == 0 and num[0] == 1:  # need to roll back to 9's with 1 less digit
                result = '9' * (len(num)-1)
                break

            # Decrease the index, replace with 9's
            num[decrease_index] -= 1

            result = ''.join(str(x) for x in num[0:decrease_index+1]) + '9' * (len(num)-(decrease_index+1))

            for k in xrange(decrease_index+1, len(num)):
                num[k] = 9

            break

    if result == '': # number is fine
        result = line

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
