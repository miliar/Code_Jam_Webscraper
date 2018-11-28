import math
fin = open('C.in', 'r')
fout = open('C.out', 'w')


def pow_2(x):
    return int(math.log(x, 2))

def compute(n, k):
    if (n, k) == (2, 1):
        return (1, 0)
    if n - k <= 1:
        return (0, 0)
    # find the smallest x s.t. k < 2^x - 1
    p = pow_2(k)
    num_buckets = 2 ** p
    # subtract 2^p - 1 partitions from n
    avail = n - (num_buckets - 1)
    bucket_size = float(avail) / num_buckets 
    nth_bucket = k - (num_buckets - 1)
    width_big = math.ceil(bucket_size) 
    width_small = math.floor(bucket_size) 
    check = width_big * nth_bucket + width_small * (num_buckets - nth_bucket)
    if check > avail:
        # we have to round down
        width = math.floor(bucket_size)
    else:
        width = math.ceil(bucket_size)
    final = (width - 1) / 2
    x = int(math.ceil(final))
    y = int(math.floor(final))
    return (x, y)

T = int(fin.readline())
for t in range(1, T+1):
    N, K = map(int, fin.readline().split())
    y, z = map(str, compute(N, K))
    fout.write('Case #' + str(t) + ': ' + y + ' ' + z + '\n')
