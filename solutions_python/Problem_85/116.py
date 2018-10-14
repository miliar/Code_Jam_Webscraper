'''
Created on May 21, 2011

@author: karnr
'''
import bisect

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        input_list = map(int, fh.readline().strip().split())
        
        test_data[count] = input_list
        
        count = count + 1
    
    fh.close()
    return test_data

def _execute_test(input_list):
    boosters = input_list[0]
    boost_time = input_list[1]
    stars = input_list[2]
    constant = input_list[3]
    hops = input_list[4:]
    
    print "\n====Input: %s" % input_list
    
    assert constant == len(hops)
    distance = list()
    idx = 0
    while (idx < stars):
        distance.extend(hops)
        idx += constant
        
    distance = distance[0:stars]
    
    assert len(distance) == stars
    
    time = map(lambda x: 2 * x, distance)
    
    print "Distance: %s" % distance
    print "Time: %s" % time
    
    cum_time = [sum(time[:i+1]) for i in range(len(time))]
    total_time = cum_time[-1]
    print cum_time
    
    index = bisect.bisect_left(cum_time, boost_time)
    
    new_time = list()
    new_time.extend(time)
      
    if index < len(cum_time):
        for i in range(index+1):
            if cum_time[i] <= boost_time:
                new_time[i] = 0
            else:
                new_time[i] =  cum_time[i] - boost_time
            
        print new_time
        new_time.sort(reverse=True)
        print new_time
    
        for i in range(boosters):
            dst = new_time[i]
            #print dst
            total_time = total_time - (dst/2)
         
    print total_time
    return total_time

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()