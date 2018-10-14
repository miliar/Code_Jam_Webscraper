def get_map():
    #from input/output example
    inp = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    out = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

    map = {}

    for idx, char in enumerate(inp):
        map[char] = out[idx]

    #from example in the description text
    map['q'] = 'z'
    map['z'] = 'q'
    map['\n'] = '\n'

    return map

def g_to_e(inp):
    map = get_map()
    output = ""
    for char in inp:
        eng = map[char]
        output += eng
    return output
        
    

def read_file(fname):
    f = open(fname,'r')
    fw = open(fname+'_out','w+')
    T = f.readline()
    for i in range(1,int(T)+1):
        googlerese = f.readline();
        english = g_to_e(googlerese)
        fw.write("Case #{}: {}".format(i,english))

if __name__ == '__main__':
    read_file('inp_A')