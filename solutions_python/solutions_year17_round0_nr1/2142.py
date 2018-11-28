import sys

def get_minimal(bits, k):
    i = 0
    cnt = 0
    bits_len = len(bits)
    while (i < bits_len):
        if bits[i] == 0 and (i <= bits_len - k):
            cnt += 1
            for j in xrange(k):
                bits[i + j] ^= 1
        if bits[i] == 0 and (i > bits_len - k):
            return "IMPOSSIBLE"
        i += 1
    return cnt

def print_resp(i, res):
    print "Case #{i}: {res}".format(i=i, res=res)

def prcs_data():
    t = int(raw_input())
    vals = []
    for i in xrange(t):
        s, k = raw_input().split(" ")
        k = int(k)
        nums = map(lambda x: 1 if x == "+" else 0, s)
        res = get_minimal(nums, k)
        print_resp(i+1, res)

if __name__ == "__main__":
    prcs_data()