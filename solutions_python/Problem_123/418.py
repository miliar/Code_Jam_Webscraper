import sys

#if len(sys.argv) != 3:
#    print("Usage: python scriptA.py <input_file> <output_file>")
#    exit()
#
#input_file = sys.argv[1]
#output_file = sys.argv[2]

input_file = 'A-large.in'
output_file = 'A-large.out'

def min_num_steps(A, arr):
    cnt = 0
    larr = len(arr)
    tmp = [A]
    min_num = larr
    n = 0
    while n < larr:
        if A > arr[n]:
            tmp.append(tmp[-1] + arr[n])
            A += arr[n]
            n += 1
        else:
            rem_num = cnt + larr - n
            if min_num > rem_num: min_num = rem_num
            if cnt > min_num: break
            cnt += 1
            A += A - 1

    if cnt < min_num: min_num = cnt

    return tmp, min_num

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for t in xrange(0,T):
        line = f.readline()
        A, N = tuple(map(int, line.split(' ')))
        line = f.readline()
        arr = map(int, line.split(' '))
        arr.sort()
        narr, mns = min_num_steps(A, arr)
        results.append('Case #' + str(t + 1) + ': ' + str(mns) + '\n')

with open(output_file, 'w') as f:
        f.writelines(results)

