def is_recyc(a, b):
    a_s = str(a)
    #check if numbers less than or equal to b can be made by shuffling a
    result = []
    temp = a_s
    for i in range(len(a_s)):
        temp = temp[-1] + temp[:-1]
        check = int(temp)
        #must be less than B and ones less than a are covered by others
        if (check <= b) and (check > a):
            result = result + [[a, check]]
    return result

def check_range(A,B):
    all_range = []
    for i in range(A,B+1):
        all_range = all_range + is_recyc(i,B)
    #want distinct ones only
    final = []
    for item in all_range:
        if not item in final:
            final = final + [item]
    return final

def solve_lines(lines):
    tests = int(lines[0])
    out = ""
    for i in range(1,tests+1):
        out = out + "Case #" + str(i) + ": "
        split = lines[i].split(' ')
        out = out + str(len(check_range(int(split[0]),int(split[1])))) + "\n"
    
    return out

def solve_file(filename):
    f = open(filename)
    l = []
    for line in f:
        l = l + [line.replace("\n", "")]
    f.close()
    return solve_lines(l)

a = solve_file('C-small-attempt0.in')
b = open('C-out', 'w')
b.write(a)
b.close()