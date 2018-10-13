verbose=False
def solve(interval):#inclusive
    a,b=[int(i) for i in interval.split()]
    counter=0
    for i in xrange(a,b+1):
        #python 2.7.3 xrange throws
        #OverflowError: Python int too large to convert to C long
        #and range (tries to) create too large list...
        #print i
        if str(i)!=str(i)[::-1]:
            if verbose:print(i,'not palindrome [number]')
        else:
            root="{:g}".format(i**.5)
            # slower on py3k?
            if str(root)!=str(root)[::-1]:
                if verbose:print(root,'not palindrome [root]')
                pass
            else:
                if verbose:print(i," is counted")
                counter+=1
    return counter

def parse():
    with open("input", "r") as f_in, open("output", "w") as f_out:
        total_cases = int(f_in.readline())
        for case_num in range(total_cases):
            out="Case #{}: {}".format(case_num+1, solve(f_in.readline().strip()))
            f_out.write(out+"\n")

if __name__ == '__main__':
    parse()