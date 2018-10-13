import re, sys

def stall_rechunk(chunk_sizes):
    max_chunk = max(chunk_sizes)
    left = (max_chunk - 1) // 2
    right = max_chunk // 2
    chunk_sizes[max_chunk] -= 1
    if chunk_sizes[max_chunk] == 0 : del chunk_sizes[max_chunk]
    if left in chunk_sizes: chunk_sizes[left] += 1
    elif left !=0: chunk_sizes[left] = 1
    if right in chunk_sizes: chunk_sizes[right] += 1
    elif right !=0: chunk_sizes[right] = 1

def get_max_min(chunk_sizes):
    max_chunk = max(chunk_sizes)
    M = max_chunk // 2
    m = (max_chunk - 1) // 2
    return (M,m)

def sol(N,K):
    chunk_sizes = {N:1}
    for i in range(K-1):
        stall_rechunk(chunk_sizes)
    return get_max_min(chunk_sizes)
    
def parse(file_name, outfile_name, func):
    file = open(file_name,"r")
    lines = (line.rstrip('\n') for line in file.readlines())
    file.close()
    cases = int(lines.__next__())
    out = open(outfile_name,"w")
    for i in range(cases):
        args = re.split(' ', lines.__next__())
        args[0] = int(args[0])
        args[1] = int(args[1])
        output = func(*args)
        out.write('Case #{0}: {1} {2}'.format(i+1,output[0],output[1]) + '\n')
    out.close()
    return

#usage (run using python3): python C.py 'input_filepath' 'output_filename'

if __name__ == '__main__':
    parse(sys.argv[1], sys.argv[2], sol)
