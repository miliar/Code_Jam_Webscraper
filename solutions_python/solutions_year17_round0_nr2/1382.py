import re,sys

def tidy_fail(int_string):
    strng = int_string[::-1]
    out = None
    t = len(int_string)
    for i in range(t-1):
        if strng[i] < strng[i+1]: return i
    return out

def iter_tidy(int_string):
    #one tidying move
    i = tidy_fail(int_string)
    if i == None: return int_string
    head = int_string[:-(1 + i)]
    int_string = head +  ('9' * (len(int_string)-len(head)))
    int_val = int(int_string)
    int_val -= 10 ** (i + 1)
    return  str(int_val)

def sol(int_string):
    while tidy_fail(int_string) != None:
        int_string = iter_tidy(int_string)
    return int_string

def parse(file_name, outfile_name, func):
    file = open(file_name,"r")
    lines = (line.rstrip('\n') for line in file.readlines())
    file.close()
    cases = int(lines.__next__())
    out = open(outfile_name,"w")
    for i in range(cases):
        args = re.split(' ', lines.__next__())
        output = func(*args)
        out.write('Case #{0}: {1}'.format(i+1, output) + '\n')
    out.close()
    return

#usage (run using python3): python B.py 'input_filepath' 'output_filename'

if __name__ == '__main__':
    parse(sys.argv[1], sys.argv[2], sol)
    

    
        
    
    
    
    
    
