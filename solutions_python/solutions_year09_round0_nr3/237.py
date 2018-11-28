BASE_STRING = 'welcome to code jam'

def cut_down(i):
    if i <= 9999:
        return i
    b = int(i / 10000)
    return i - b * 10000

def iter_str(stri):
    global COUNT
    COUNT = 0
    chr_list = [-1] * len(BASE_STRING)
    find_all(stri, 0, chr_list)
    return COUNT

def find_all(s, i, chr_list):
    global COUNT
    num_results = 0
    while True:
        out = s.find(BASE_STRING[i], max(0, chr_list[i]+1))
        #print 'Found %s at %s' % (BASE_STRING[i], out)
        if out == -1:
            #print '  No more. Returning %s...' % num_results
            return num_results
        chr_list[i:] = [out]*len(chr_list[i:])
        if i == len(BASE_STRING) - 1:
            COUNT += 1
            num_results += 1
            #print '  Done! %s' % COUNT
        else:
            find_all(s, i + 1, list(chr_list))
    
in_file = open('c_in.txt','r')
num = int(in_file.readline().strip())
for l in (x + 1 for x in range(num)):
    line = in_file.readline()
    n = iter_str(line)
    print 'Case #%s: %04i' % (l, cut_down(n))
