# in_filename = "test-in.txt"
in_filename = "A-small-attempt1.in.txt"
# in_filename = "A-large.in"
h = open(in_filename, 'r')


ncases = int(h.readline().strip())
for case in xrange(1, ncases+1):
    message = h.readline().strip()
    
    digits = []
    for dig in message:
        if dig not in digits:
            digits.append(dig)
    

    base = len(digits)
    result = None
    if len(digits) == 1:
        result = int("1"*len(message), 2)
    else:
        for i in xrange(len(digits)):
            for j in xrange(len(digits)-1):
                digits[j], digits[j+1] = digits[j+1], digits[j]
            
            
                # print digits
                dmessage = []
                for dig in message:
                    dmessage.append(str(digits.index(dig)))
            
                # print dmessage, int("".join(dmessage), base)
                new_number = int("".join(dmessage), base)
                if result is None and dmessage[0] != '0':
                    result = new_number
                elif new_number<result and dmessage[0]!='0':
                    result = new_number
    print "Case #%s: %s" % (case, result)


h.close()