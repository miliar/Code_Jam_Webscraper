from collections import defaultdict

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        nset = map(int, fh.readline().strip().split())
        test_data[count] = nset
        count = count + 1

    fh.close()
    return test_data

def _execute_test(test_data):
    n = test_data[0]
    nlist = test_data[1:]
    assert len(nlist) == n
    print nlist
    scores = defaultdict(list)

    for x in nlist:
        #print "\n*** "
        for k in scores.keys():
            #print "\n***** "
            #print x, k, scores
            new_score = x + k
            #print new_score
            if new_score in scores:
                old_list = list(scores[k])
                old_list.append(x)
                new_list = scores[new_score]
                inter = filter(lambda x: x in old_list, new_list)
                if len(inter) == 0:
                    return "\n%s" % "\n".join([" ".join(map(str, old_list)), " ".join(map(str, new_list))])
                    #return ''
            else:
                scores[new_score].append(x)
                scores[new_score].extend(scores[k])
            #print scores

        if x in scores:
            return "\n%s" % "\n".join([str(x), " ".join(map(str, scores[x]))])
            #return ''
        else:
            scores[x].append(x)
        #print scores
        
    #print scores
    
    return ''

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))

    print "Done"
    output.close()

if __name__ == '__main__':
    main()