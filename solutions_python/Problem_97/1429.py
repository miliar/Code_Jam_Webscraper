
# return the number of max possibilities
def hanlde_input(input):
    input_list = input.split(" ")
    
    result = 0
    
    A = int(input_list[0])
    B = int(input_list[1])
    
    str_a = str(A)

    length = len(str_a)
    
    if length == 1:
        return 0
    r = range(A,B+1)
        
    for i in r:
        tmp = 2 * str(i)
        checked = set()
        for j in range(length):
            tmp1 = int(tmp[j:j + length])
            if tmp1 in checked:
                continue
            checked.add(tmp1)
            if i >= tmp1:
                continue
            if tmp1 in r:
                result = result + 1
    
    return result

def solve():
    file_in = file("C-small-attempt0.in")
    file_out = file("C-small-attempt0.out","w")
    num_of_cases = int(file_in.readline())
    lines = []
    for i in range(num_of_cases):
        # read
        line = file_in.readline()
        
        # process
        result = hanlde_input(line)
        
        # write
        lines.append('Case #%s: %s\n' % (i+1,result))
    
    file_out.writelines(lines)
    file_out.close()

if __name__ == '__main__':
    solve()