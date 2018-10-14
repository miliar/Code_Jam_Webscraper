import sys

def is_tidy(n):
    n_lst = list(n)
    for i in range(1,len(n_lst))[::-1]:
        if int(n_lst[i-1])>int(n_lst[i]):
            n_lst[i-1]=str(int(n_lst[i-1])-1)
            for j in xrange (i,len(n_lst)):
                n_lst[j] = '9'


    return ''.join(n_lst).lstrip('0')

output = []

with open(sys.argv[1], 'rb') as input_file:
    inp = input_file.readlines()
for line_num in range(1, int(inp[0])+1):
    output.append('Case #'+str(line_num)+': '+is_tidy(inp[line_num].strip()))
    output.append("\r\n")
output.pop()
print output
with open(sys.argv[2], 'wb') as out:
    out.writelines(output)
