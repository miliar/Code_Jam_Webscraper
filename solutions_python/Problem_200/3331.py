def tidy_number(n):

    n_str=str(n)
    S = len(n_str)

    n_list=[]
    for d in range(S):
        n_list.append(int(n_str[d]))

    for i in range(S-1):
        if n_list[S-1-i]<n_list[S-1-(i+1)]:
            n_list[S-1-(i+1)]-=1
            for j in range(i+1):
                n_list[S-1-j]=9

    s = map(str, n_list)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)

    return s



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())  # read a list of integers, 2 in this case
    print("Case #{}: {}".format(i, tidy_number(n)))
    # check out .format's specification for more formatting options