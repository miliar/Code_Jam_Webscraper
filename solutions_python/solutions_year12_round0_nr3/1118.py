import sys

def main(raw_data):
    data = []
    for line in raw_data:
        data.append(line.strip())
        
    recycled_dict = {}
    checked_lengths = set()
        
    T = data.pop(0)
    for i in range(int(T)):
        start, end = data.pop(0).split(' ')
        #print start, end
        if len(start) not in checked_lengths:
            #compile the recycled pairs of this length
            #print "compiling"
            length = len(start)
            for j in range(10**(length-1), 10**length):
                string = str(j)
                #generate and check the variations on this number
                for k in range(1, length):
                    first = string[:k]
                    second = string[k:]
                    new_number = '%s%s' % (second, first)
                    new_number = int(new_number)
                    if j != new_number and len(str(new_number)) == length:
                        if not recycled_dict.has_key(j):
                            recycled_dict[j] = []
                        recycled_dict[j].append(new_number)
            checked_lengths.add(length)
            #print "dict is now", len(recycled_dict)
        
        #print 'countting'
        
        #now, count how many are between these numbers
        count = 0
        start = int(start)
        end = int(end)
        found_sets = set()
        for num, values in recycled_dict.items():
            if num >= start and num <= end:
                for value in values:
                    if num < value and value >= start and value <= end:
                        check_str = "%s-%s" % (num, value)
                        if check_str not in found_sets:
                            count += 1
                            found_sets.add(check_str)
                            
        print "Case #%s: %s" % (i+1, count)
                
if __name__ == "__main__":
    main(sys.stdin)
