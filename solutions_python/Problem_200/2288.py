
def print_resp(i, res):
    print "Case #{i}: {res}".format(i=i, res=res)

def get_maxi(N, fmin=0):
    if fmin > N[0]:
        return -1
    if len(N) == 1:
        return N

    res = get_maxi(N[1:], fmin=N[0])
    if res != -1:
        return ([N[0]] + res)
    elif (N[0] - 1) >= fmin:
        nlen = len(N)
        return ([N[0] - 1] + (nlen-1)*[9])
    else:
        return -1

def prcs_data():
    t = int(raw_input())
    vals = []
    for i in xrange(t):
        N = raw_input()
        res = get_maxi([int(ch) for ch in N])
        res = str(int(''.join(map(str, res))))
        print_resp(i + 1, res)

if __name__ == "__main__":
    prcs_data()
