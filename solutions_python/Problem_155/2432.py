case_number = 1
def read_input_file_line_by_line():
    with open('A-Large.in', 'r')  as testfile:
        x = 0
        for line in iter(testfile):
            cases = line.split("\n")[0].split(" ")
            cases_dict = {}
            cases_dict['max_si'] = int(cases[0])
            
            if x==0:
                x=x+1
                #print "Number of test cases", cases[0]
                continue
            cases_dict['si_levels'] = cases[1]
            get_friends_required_in_audiance(cases_dict)
            x=x+1
def get_friends_required_in_audiance(cases_dict=None):
    global case_number
    number_of_freinds_required = 0
    number_of_people_standing = 0
    i=0
    for people_with_si in cases_dict['si_levels']:
        number_of_people_standing += int(people_with_si)
        if number_of_people_standing < i + 1:
            number_of_freinds_required += i + 1 - number_of_people_standing
            number_of_people_standing += i + 1 - number_of_people_standing
            
        i+=1
    print "Case #%d: %d"% (case_number,number_of_freinds_required)
    case_number +=1
if __name__ == '__main__':
    read_input_file_line_by_line()
    