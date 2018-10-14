__author__ = 'narun'


def write_output(fh, case, output_list):
    fh.write('Case #'+str(case)+': '+''.join(output_list)+'\n')


filename = 'B-large.in'
outfile = 'B-large.out'
# filename = 'A-large-practice.in'
# outfile = 'A-large-practice.out'
input_file = open(filename, 'r')
output_file = open(outfile, 'w')
debug = False

num = int(input_file.readline())
for i in range(num):
    # credit = int(input_file.readline())
    # item = int(input_file.readline())
    text = input_file.readline()
    arr = text.split()
    c = float(arr[0])
    f = float(arr[1])
    x = float(arr[2])
    nc = 0
    t = 0
    print(c, f, x) if debug else None
    # while nc*c/2 + x/(2+nc*f) > (nc+1)*c/2 + x/(2+(nc+1)*f):
    while x/(2+nc*f) > c/(2+nc*f) + x/(2+(nc+1)*f):
        t += c/(2+nc*f)
        nc += 1
        print(t) if debug else None
    t += x/(2+nc*f)
    print(t) if debug else None
    write_output(output_file, i+1, ["%.7f" % t])