import fileinput


def main():
    """Tidy some numbers"""
    cases = []
    case_counter=0
    for line in fileinput.input():
        if fileinput.isfirstline():
            num_cases=line.strip()
        else:
            case_counter = case_counter + 1
            counted_to = line.strip()
            cases.append( (case_counter, counted_to) )


    for case in cases:
        calc_case(*case)


# 132 -> 129
# 1000 -> 999
# 7 -> 7
# 111111111111111110 -> 99999999999999999

def calc_case(case_num, counted_to):
    if is_tidy(counted_to):
        print "Case #%d: %s" % (case_num, counted_to)
    else:
        print "Case #%d: %s" % (case_num, make_tidy(counted_to))


def is_tidy(num_str):
    str_len = len(num_str)
    if str_len==1:
        return True
    else:
        pos=1
        while pos<str_len:
            #print pos
            #print "checking %s and %s" % (num_str[pos-1],num_str[pos],)
            if num_str[pos-1]>num_str[pos]:
                return False
            pos= pos + 1
    return True


def make_tidy(num_str):
    str_len = len(num_str)
    pos=str_len-1
    result=[]
    reduce_left_digit=False
    while pos>=0:
        #print pos

        if pos>0:
            first=num_str[pos-1]
            second=num_str[pos]

            if reduce_left_digit:
                second=chr(ord(second) - 1)

            #print "checking %s and %s" % (first, second,)

            if first<=second:
                result.append(second)
                #print "case 1 adding %s" % (second,)
                reduce_left_digit = False
                pos=pos-1
            else:
                if False: #second=='0':
                    #print "can't handle this yet"
                    result.append(second)
                    #print "case 2 adding %s" % (second,)
                    pos = pos - 1
                else:
                    #carried_digit=chr(ord(first)-1)
                    #result.append(carried_digit)
                    result.append('9')
                    #print "case 3 adding 9"
                    reduce_left_digit=True
                    pos = pos - 1
        else:
            if reduce_left_digit:
                if num_str[0]=='1':
                    #print "case 5 skipping digit"
                    pass
                else:
                    result.append(chr(ord(num_str[0]) - 1))
                    #print "case 6 adding %s" % (chr(ord(num_str[0]) - 1),)
            else:
                result.append(num_str[0])
                #print "case 7 adding %s" % (num_str[0],)
            pos = -1


    result.reverse()

    final_result=[]
    min_val=result[0]
    for c in result:
        if c < min_val:
            final_result.append(min_val)
        else:
            final_result.append(c)
            min_val=c

    return "".join(final_result)



if __name__ == '__main__':
    main()
