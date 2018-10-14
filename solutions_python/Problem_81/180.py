from __future__ import division
import sys

if not len(sys.argv) == 3:
    exit("""Wrong usage parameters supplied!
    
    Usage:
    %s input output""" % __file__
    )
    
def solve(table):
    wp = []
    for r in table:
        wp_num = 0
        wp_denom = 0
        for res in r:
            if res != '.':
                wp_denom += 1
                if res == '1':
                    wp_num += 1
        wp.append((wp_num, wp_denom))
    owp = []
    
    opponents_nums = []
    for i in xrange(len(table)):
        owp_cur = 0
        opponents_num = 0
        for k in xrange(len(table)):
            if i != k:
                wp_cur = wp[k]
                num = wp_cur[0]
                denom = wp_cur[1]
                if table[k][i] != '.':
                    denom -= 1
                    if table[k][i] == '1':
                        num -= 1
                    opponents_num += 1
                    owp_cur += num / denom
        opponents_nums.append(opponents_num)
        owp.append(owp_cur / opponents_num)
    oowp = []
    for i in xrange(len(table)):
        oowp_cur = 0
        for k in xrange(len(table)):
            if i != k:
                if table[k][i] != '.':
                    oowp_cur += owp[k] / opponents_nums[i]
        oowp.append(oowp_cur)
    rpis = []
    for i in xrange(len(table)):
        wp_cur = wp[i]
        rpis.append(0.25*(wp_cur[0]/wp_cur[1]) + 0.5*owp[i] + 0.25*oowp[i])
    return rpis

def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):
            
            n = int(input_f.readline().strip())
            table = []
            for i in xrange(n):
                table.append(input_f.readline().strip())
                
            rpis = solve(table)
            
            output_f.write("Case #%d:\n" % (test_case_i + 1))
            for f in rpis:
                output_f.write("%.12g\n" % f)
    
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
