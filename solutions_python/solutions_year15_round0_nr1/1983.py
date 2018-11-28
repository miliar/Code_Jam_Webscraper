import sys
################################################################################
#
################################################################################
def get_file_as_string(path):
    f = open(path, 'r')
    res = f.read()
    f.close()
    return res 
################################################################################
#
################################################################################
def get_structured_data_from_data_in(data_in):
    tmp = data_in.split("\n")
    nbr_of_cases = int(tmp[0])
    i = 1
    cases = []
    while i <= nbr_of_cases:
        string_case = tmp[i].split(" ")
        print(string_case)
        j = 0 
        case = []
        s_max = int(string_case[0]);
        while j <= s_max:
            case.append(int(string_case[1][j]))
            j+=1
        cases.append(case)
        i+=1
    return cases
################################################################################
#
################################################################################
def rearange_structured_data_in(structured_data):
    None
################################################################################
#
################################################################################
def get_data_out_from_structured_data_in(structured_data):
    res = []
    for case in structured_data:
        actual_nbr = case[0]
        case_solution = 0
        j = 1
        while j < len(case):
            if j > actual_nbr:
                case_solution += j - actual_nbr
                actual_nbr += j - actual_nbr
            actual_nbr += case[j]
            j += 1
        res.append(case_solution)
    return res
################################################################################
#
################################################################################
def print_structured_data_out(path, structured_data_out):
    f = open(path, 'w+')
    f.write("Case #1"+": "+str(structured_data_out[0]))
    i = 1
    while i < len(structured_data_out):
        f.write("\nCase #"+ str(i+1)+": "+str(structured_data_out[i]))
        i += 1
    f.close()
################################################################################
#
################################################################################
if __name__ == "__main__":
    print("START")
    data_in_as_string = get_file_as_string(sys.argv[1])
    data_in = get_structured_data_from_data_in(data_in_as_string)
    #rearange_structured_data_in(data_in)
    data_out = get_data_out_from_structured_data_in(data_in)
    print_structured_data_out(sys.argv[2], data_out)
    print("END")
