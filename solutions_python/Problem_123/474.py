def write_sol(case_no, res):
    f = open("output.txt", "a")
    f.write("Case #" + str(case_no) + ": " + str(res) + "\n")
    f.close()

def get_add_op(A,S):
    op = 1
    A += A
    A -= 1
    while A <= S:        
        op += 1
        A += A
        A -= 1
    return [A,op]

def solve(case_no, A, N, motes):
    no_op = 0
    min_op = N + 1
    if A == 1:
        write_sol(case_no, N)
        return
    motes.sort()
    for i in range(N):
        mote = motes[i]
        if A > mote:
            A += mote
        else:
            if min_op > N:
                min_op = N - i
                
            res = get_add_op(A, mote)
            if res[1] >= N - i:
                write_sol(case_no, no_op + N - i)
                return
            elif no_op + res[1] >= min_op:
                write_sol(case_no, min_op)
                return
            else:
                no_op += res[1]
                A = res[0] + mote
    write_sol(case_no, no_op)


def main():
    f = open("C:\\Documents and Settings\\user\\My Documents\\Downloads\\A-large.in", "r")
    #f = open("input.txt", "r")
    no_tests = int(f.readline())
    for i in range(0, no_tests):
        A, N = [int(x) for x in f.readline().split()]
        motes = []
        strline = f.readline()
        for x in strline.split():
            motes.append(int(x))
        solve(i+1, A, N, motes)        
    f.close()
    
print "start"
    
main()

print "end"
