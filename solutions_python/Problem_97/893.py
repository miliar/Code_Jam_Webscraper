import sys
in_file = sys.argv[1]
f = open(in_file, 'r')
input_array,output_array = [],[]
for line in f:
    input_array += [line.rstrip()]
input_array = input_array[1::]
def is_permutation(s1,s2):
    if s1 == s2: return False #should never happen
    st = s1[1:] + s1[0]
    while not st == s1 and not st == s2:
        st = st[1:] + st[0]
    if st == s2: return True
    else: return False
def count_vals(case):
    under,over = int(case.split(' ')[0]),int(case.split(' ')[1])
    count = 0
    for i in range(under,over+1):
        for j in range(i+1,over+1):
            if is_permutation(str(i),str(j)): count += 1
    if count: return str(count)
    else: return '0'
for case in input_array:
    output_array += ['Case #'+str(len(output_array)+1)+': '+count_vals(case)]
for line in output_array:
    print line
