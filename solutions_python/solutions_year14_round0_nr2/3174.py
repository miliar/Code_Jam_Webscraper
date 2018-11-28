import os


def solve(f):
    q,w,e = f.readline().split()
    c = float(q)
    f = float(w)
    x = float(e)
    t = x/2.0
    extra_t = 0.0
    p = 2.0
    while (extra_t+c/p+x/(p+f) < t):
        t = extra_t+c/p+x/(p+f)
        extra_t += c/p
        p += f
    return t


if __name__ == "__main__":
    input_filename = 'B-large.in'
    output_filename = 'googleB0.txt'
 
    f_in = open(input_filename)
    counter = int(output_filename.split('.')[0][-1])
    while os.path.isfile(output_filename):
        counter += 1
        output_filename = output_filename.split(str(counter - 1) + '.')[0] + str(counter) + '.txt'
    f_out = open(output_filename, 'a')
 
    test_cases = int(f_in.readline())
    for i in range(test_cases):
        ans = solve(f_in)
        f_out.write('Case #' + str(i + 1) +': ' + str(ans) + '\n')
 
    f_in.close()
    f_out.close()
    print "done"
