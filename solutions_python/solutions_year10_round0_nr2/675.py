def main(filename):
    
    f = open(filename)
    out = open('fair_warning.out', 'w')
    counter = 1
    case_number = 0
    for line in f:
        if counter == 1:
            C = int(line.strip())
        else:
            case_number += 1
            event_list = line.split()[1:]
            i = 0
            for item in event_list:
                event_list[i] = int(event_list[i])
                i += 1
            res = fair_warning(event_list)
            output_line = "Case #%d: %d\n" % (case_number, res)
            out.write(output_line)
        counter += 1
        
def fair_warning(event_list):
    
    d = dict()
    d = d.fromkeys(event_list)
    event_list = d.keys()
    d = diff_list(event_list)
    gcd = gcd_list(d)
    if (event_list[0] % gcd == 0):
        return 0
    else:
        return ((event_list[0] / gcd) + 1) * gcd - event_list[0]

def diff_list(numbers):

    diff_list = list()
    cur_index = 0
    for n in numbers[:-1]:
        for m in numbers[cur_index + 1:]:
            diff = abs(n - m)
            diff_list.append(diff)
        cur_index += 1
    return diff_list

def gcd_list(l):
    
    cur_gcd = l[0]
    for i in l:
        cur_gcd = gcd_2(cur_gcd, i)
    return cur_gcd
        
def gcd_2(a, b):
    
    if a > b:
        for i in range(1,b + 1):
            if b % i == 0:
                if a % i == 0:
                    result = i
        return result
    elif a < b:
        for i in range(1,a + 1):
            if a % i == 0:
                if b % i == 0:
                    result = i
        return result
    else:
        return a
    
if __name__ == "__main__":
    
    main('B-small-attempt0.in')
            