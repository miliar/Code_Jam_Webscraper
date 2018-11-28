
def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    line_num = int(data[0].strip())
    lines = [data[i].strip() for i in xrange(line_num + 1)]
    lines = lines[1:]
    assert len(lines) == line_num
    
    return lines
 
def get_num(a, b, mult):
    """
    Getting number of recycled between a and b
    """
    
    num = 0
    for i in range(a, b + 1):
        curr_rec = i / 10 + (i % 10) * mult
        while curr_rec != i:
            if curr_rec >= a and curr_rec <= b:
                num += 1
            curr_rec = curr_rec / 10 + (curr_rec % 10) * mult
                
    return num / 2
    
def get_nums(lines):
    nums = []
    for line in lines:
        print '-'*20
        (a, b) = line.split(' ')
        dig_num = len(a)
        mult = 1
        for _ in xrange(dig_num - 1):
            mult *= 10
        a = int(a)
        b = int(b)
        
        nums.append(get_num(a, b, mult))
        
    return nums

def create_output(nums):
    with file('output1.txt', 'wt') as f:
        for (i, num) in enumerate(nums):
            print >> f, 'Case #%d: %d' % (i + 1, num) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    nums = get_nums(data)
    create_output(nums)

if __name__ == "__main__":
    main()