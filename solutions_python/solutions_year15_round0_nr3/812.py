import math
import time
import sys
import operator

def reduce(start, str, table):
    result = start
    for ch in str:
        result = table[(result, ch)]
    #print result
    return result

if __name__ == '__main__':
    
    # Start timer
    start = time.time()

    if len(sys.argv) != 3:
        print 'Usage: python problemC.py <input_file> <output_file>'
        sys.exit(0)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    lines = [line.strip() for line in open(input_file)]
    total = lines.pop(0)
    #print total
    #print lines
    LX = lines[0:][::2]
    LX = [map(int,t.split()) for t in LX]
    S = lines[1:][::2]
    for i in range(len(LX)):
        # Complete the full string
        S[i] = S[i]*LX[i][1]
        # Get the total number of characters
        LX[i].append(LX[i][0]*LX[i][1])
    results = []

    table = {('1','1'):'1', ('1','i'):'i', ('1','j'):'j', ('1','k'):'k', ('1','-1'):'-1', ('1','-i'):'-i', ('1','-j'):'-j', ('1','-k'):'-k',
                ('i','1'):'i', ('i','i'):'-1',('i','j'):'k', ('i','k'):'-j', ('i','-1'):'-i', ('i','-i'):'1',('i','-j'):'-k', ('i','-k'):'j',
                ('j','1'):'j', ('j','i'):'-k',('j','j'):'-1', ('j','k'):'i', ('j','-1'):'-j', ('j','-i'):'k',('j','-j'):'1', ('j','-k'):'-i',
                ('k','1'):'k', ('k','i'):'j',('k','j'):'-i', ('k','k'):'-1', ('k','-1'):'-k', ('k','-i'):'-j',('k','-j'):'i', ('k','-k'):'1',
                ('-1','1'):'-1', ('-1','i'):'-i',('-1','j'):'-j', ('-1','k'):'-k',
                ('-i','1'):'-i', ('-i','i'):'1',('-i','j'):'-k', ('-i','k'):'j',
                ('-j','1'):'-j', ('-j','i'):'k',('-j','j'):'1', ('-j','k'):'-i',
                ('-k','1'):'-k', ('-k','i'):'-j',('-k','j'):'i', ('-k','k'):'1',}

    for case in range(len(LX)):
        number = LX[case]
        content = S[case]
        #print number
        #print content
        if number[2] < 3:
            print "case:", case+1, "NO"
            results.append("NO")
            continue
        if number[2] == 3:
            if content == 'ijk':
                print "case:", case+1, "YES"
                results.append("YES")
            else:
                print "case:", case+1, "NO"
                results.append("NO")
            continue
        # Memoize the result for comptuted substring
        left_result = ['1']
        right_result = ['1']
        # total cases, 0:number[2]-2 ways to make first split happen
        found = False
        all_i = []
        all_k = []
        for i in range(0, number[2]-2):
            #print i, left_result[i]
            #print i, content[i]
            current_left = table[(left_result[i], content[i])]
            left_result.append(current_left)
            #print i, left_result
            if current_left == 'i':
                #print "Found i"
                all_i.append(i)
        #print all_i
        for k in range(number[2]-1, 1, -1):
            #print k, right_result[number[2]-1-k]
            #print k, content[k]
            current_right = table[(content[k],right_result[number[2]-1-k])]
            right_result.append(current_right)
            #print i, right_result
            if current_right == 'k':
                #print "Found k"
                all_k.append(k)
        #print all_k
        #print content
        all_k.reverse()
        for i_idx in range(len(all_i)):
            temp_result = '1'
            for k_idx in range(len(all_k)):
                if all_k[k_idx] <= all_i[i_idx]+1:
                    continue
                if k_idx>0 and all_k[k_idx-1] > all_i[i_idx]+1:
                    temp_middle = content[all_k[k_idx-1]:all_k[k_idx]]
                else:
                    temp_middle = content[all_i[i_idx]+1:all_k[k_idx]]
                #print all_k[k_idx]
                #print all_i[i_idx]+1
                #print middle
                temp_result = reduce(temp_result, temp_middle, table)
                if temp_result == 'j':
                    found = True
                    break
            if found:
                break
        if found:
            print "case:", case+1, "YES"
            results.append("YES")
        else:
            print "case:", case+1, "NO"
            results.append("NO")
    print results

    # output
    f = open(output_file, 'w')
    for i in range(len(results)):
        f.write('Case #' + str(i+1) + ': ' + str(results[i])+'\n')
    f.close()

    # Stop timer
    end = time.time()
    print "Total time use:", end-start, "s"