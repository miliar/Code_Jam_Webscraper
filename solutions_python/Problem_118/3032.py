#file case_output.py
#author Colton Lewis
#date 4/3/13

def case(func, i_file, o_file):
    """
    Applies a function to each line of input file and writes output file
    in Case #: format
    """
    i=open(i_file, "r")
    o=open(o_file, "w")
    num_cases=int(i.readline())

    for x in range(1, num_cases+1):
        args=i.readline().split()
        o.write("Case #{}: ".format(x)+str(func(*args))+"\n")

    i.close()
    o.close()
