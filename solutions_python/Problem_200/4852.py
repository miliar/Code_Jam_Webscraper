with open('B-small-attempt1.in','r') as f:
    lines = f.readlines()
out  = open('output.in','w')

#getting number of testcases
try:
    T= int(lines[0])
except:
    raise("Invalid input file")

#checking file
if len(lines) == 0 or len(lines)==1 or len(lines) < T+1:
    raise Exception("Invalid input file")
lines = lines[1:]
tc_num = 1

def check_tidy(num):
    num_str = str(num)
    num_list = [int(x) for x in list(num_str)]
    sorted_num_list = sorted(num_list)
    if sorted_num_list == num_list:
        return True
    return False


def get_last_tidy(N):
    #import pdb;pdb.set_trace()
    num = N
    while(num >=0):
        num_str = str(num)
        if num_str.endswith('0'):
            num = num-1
            continue
        x = check_tidy(num)

        if x:
            return(num)
        num = num - 1
tc_num=1
for line in lines:
    N = int(line)
    output = get_last_tidy(N)

    str_output = "CASE #%d: %d" % (tc_num, output) + '\n'
    out.write(str_output)
    tc_num=tc_num+1