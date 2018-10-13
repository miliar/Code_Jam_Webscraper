def C(input):
    nums = [int(c) for c in input]
    parity = reduce(lambda a, b: a^b, nums)
    
    return str(sum(nums)-min(nums)) if parity == 0 else 'NO'    

if __name__ == '__main__':
    #str_in = 'C-test.in'
    #str_in = 'C-small-attempt0.in'
    str_in = 'C-large.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    for i, input in enumerate(open(str_in)):
        input = input.strip()
        if i == 0:
            T = [int(_s) for _s in input.split()[:1]]
            continue
        if i%2==1:
            continue
        
        output = 'Case #' + str(i/2) + ': ' + C(input.split()) + '\n'
        f_out.write(output)
        print output,

    f_out.close()
    
    print 'exit'

