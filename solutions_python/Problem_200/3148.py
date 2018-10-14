t = int(raw_input())
for i in xrange(1, t+1):
    number_list = list(raw_input())
    printed = False
    if len(number_list) == 1:
        print "Case #%d: %s" % (i, number_list[0])
        continue
    for j in xrange(len(number_list) - 1):
        if number_list[j] > number_list[j+1]:
            number_list[j] = str(int(number_list[j]) - 1)
            for k in xrange(j+1, len(number_list)):
                number_list[k] = '9'
            for k in xrange(j, 0, -1):
                if number_list[k] < number_list[k-1]:
                    number_list[k] = '9'
                    number_list[k-1] = str(int(number_list[k-1]) - 1)
            print "Case #%d: %s" % (i, str(int(''.join(number_list))))
            printed = True
            break
    if not printed:
        print "Case #%d: %s" % (i, str(int(''.join(number_list))))