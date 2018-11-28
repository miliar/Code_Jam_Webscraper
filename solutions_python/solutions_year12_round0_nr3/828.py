def all_recycled_pairs(A, B):
    counted_pairs = set([])
    count = 0
    for n in range(A, B+1):
        number = list(str(n))
        for i in range(1, len(number)):
            m = number[-i:]+number[:-i]
            new_number = int(''.join(m))
            if n<new_number and A<=new_number<=B and (n, new_number) not in counted_pairs:
                count+=1
                counted_pairs.add((n, new_number))
    return count 

input_file = open('C-small-attempt0.in')
output_file = open('recycled_out', 'w')
for i, line in enumerate(input_file.readlines()):
    if i==0:
        continue
    else:
        l = line.split()
        A = int(l[0])
        B = int(l[1])
        output_file.write('Case #%d: %d\n'%(i, all_recycled_pairs(A, B)))
input_file.close()
output_file.close()

