

def func_b():
    test_cases = int(raw_input())

    for case in xrange(1, test_cases + 1):
        # change from ints if different type
        line = raw_input()
        method(line, case)

def method(line, case):
        #handles case when integer
        output = line

        for i in xrange(0, len(line)-1):
            if line[i] <= line[i+1]:
                pass
            else:
                val = i
                while val-1 >= 0 and line[val-1] == line[val]:
                    val -= 1
                output = untidyNumber(line, val)
                break


        print "Case #%s: %s" % (case, output)

def untidyNumber(num, pos):
    if num[pos] != '1':
        return '%s%s%s' %(num[:pos], int(num[pos])-1, '9'*(len(num)-1-pos))
    else:
        return '9'*(len(num)-1)


func_b()
#method('440',1)
