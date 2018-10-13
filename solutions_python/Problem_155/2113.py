import sys

def solve(tests):
    for test_num,t in enumerate(tests):
        smax = t[0]
        shy_levels=list(t[1])
        standing = 0
        #print shy_levels
        ppl_needed=0
        for level,ppl_at_lvl in enumerate(shy_levels):
            #print "level",level," standing : ",standing
            if level == 0:
                standing = standing + int(ppl_at_lvl)
                if standing == 0:
                    standing = standing + 1
                    ppl_needed = ppl_needed + 1
                continue
            level_deficit = level - standing
            #print 'deficit :',level_deficit
            #print 'ppl_needed :',ppl_needed
            #print 'ppl_at_lvl :',ppl_at_lvl
            if level_deficit > 0:
                standing = standing + level_deficit + int(ppl_at_lvl)
                ppl_needed = ppl_needed + level_deficit
            else:
                standing = standing + int(ppl_at_lvl)
        print 'Case #'+ str(test_num+1) + ': ' + str(ppl_needed)
    
def read_file(f):
    lines = f.split("\n")[1:-1]
    tests = []

    for idx,line in enumerate(lines):
        smax,svals = line.split(' ')
        tests.append([smax,svals])

    return tests

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        tests = read_file(input_data)
        solve(tests)
    else:
        print 'Program requires an input file'
        
