import sys

def start_standing_ovation(shyness_levels):
    count = 0
    no_of_people_standing = 0
    for i in range(0, len(shyness_levels)):
        if shyness_levels[i] != 0:
            if no_of_people_standing < i:
                # you need to add frnds here.
                count += i - no_of_people_standing
                no_of_people_standing += count

            if no_of_people_standing >= i:
                no_of_people_standing += shyness_levels[i]
    return count 

def parse_line(f):
    shyness_levels = []
    input_line = f.readline()
    input_line = input_line.rstrip()
    audience_details = input_line.split()
    max_shy_level =  int(audience_details[0])
    
    tmp_str = audience_details[1]
    for i in range(0, len(tmp_str)):
        shyness_levels.append(int(tmp_str[i]))
    
    return max_shy_level, shyness_levels
 
def main():
    f = open(sys.argv[1], 'r')
    no_test_cases = f.readline()
    no_test_cases = int(no_test_cases)
    
    for i in range(1, no_test_cases + 1):
        max_shy_level, shyness_levels = parse_line(f)
        min_frnds_count = start_standing_ovation(shyness_levels)
        print 'Case #'+str(i)+':', min_frnds_count 
       
    f.close()

#This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

