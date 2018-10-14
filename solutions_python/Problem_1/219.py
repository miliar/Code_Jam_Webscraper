import os, sys

bgPrint = False

def printcm(cost_matrix):
    if bgPrint:
        for st in range(len(cost_matrix)):
            print cost_matrix[st]


def min_choice(pos, cost_m, stage):
    l = []
    for i in range(len(cost_m)):
        if i != pos:
            l.append(cost_m[i][stage])

    return min(l) + 1

def solve(case_no, se_list, q_list):
    cost_matrix = [ ]
    for i in range(len(se_list)):
        cost_matrix.append([0])

    counter = 0
    for q in q_list:
        printcm(cost_matrix)    
        counter = counter + 1
        if se_list.has_key(q):
            for se,idx in se_list.items():
                if se != q:
                    cost_matrix[idx].append(cost_matrix[idx][-1])
                else:
                    cost_matrix[idx].append(min_choice(idx, cost_matrix, counter-1))
        else:
            counter = counter - 1

    final_costs = []
    for i in range(0,len(cost_matrix)):
        final_costs.append(cost_matrix[i][-1])

    return min(final_costs)


def main():
    print "Current directory has: ", os.listdir(".")
    file_name = raw_input("Enter the file name: ")
    try:
        file_handle = file(file_name, 'r')
        num_cases = int(file_handle.readline())
        for case in range(0,num_cases):
            se_list = {}
            num_se = int(file_handle.readline())
            for se in range(0,num_se):
                se_list[file_handle.readline()] = se

            num_q = int(file_handle.readline())
            q_list = []
            for q in range(0,num_q):
                q_list.append(file_handle.readline())

#            print "se_list: ", se_list
#            print "q_list: ", q_list
            print "Case #" + str(case + 1) + ":", solve(case, se_list, q_list)
                
    except IOError, e:
        print "Bad file!"
        raw_input("Press any key to exit...")
        return 0


if __name__ == "__main__":
    main()

