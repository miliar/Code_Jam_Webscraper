import sys, os

file_in = 'A-large.in'
file_out = 'A-large.out'
#file_in = 'test.txt'
#file_out = 'test.out.txt'

f = open(file_in, 'r')
res_f = open(file_out, 'w')



def find_best(queries_list, search_engine_list):
    found_in_query_list = []
    found_num = 0
    max_len = len(search_engine_list)
    for i in range(len(queries_list)):
        q = queries_list[i]
        if q not in found_in_query_list:
            found_in_query_list.append(q)
            found_num += 1
            if found_num == max_len:
                # all search engines have been found, select this one
                return queries_list[i:]
    return []

def compute_number(queries_list, search_engine_list):
    count = -1
    while queries_list:
        queries_list = find_best(queries_list, search_engine_list)
        count += 1
    if count == -1:
        count = 0
    return count

line_num = 0
test_cases_num = 0

l = f.readline().strip('\n')
test_cases_num = int(l)
for i in range(test_cases_num):
    se_list = []
    l = f.readline().strip('\n')
    se_len = int(l)
    for j in range(se_len):
        l = f.readline().strip('\n')
        se_list.append(l)
    qe_list = []
    l = f.readline().strip('\n')
    qe_len = int(l)
    for j in range(qe_len):
        l = f.readline().strip('\n')
        qe_list.append(l)

    print >> res_f, "Case #%s: %s" % ((i+1), compute_number(qe_list, se_list))


try:
    f.close()
    res_f.close()
except:
    pass

print "done"