def google_translate(string):

    mapping = {'z':'q', 'q':'z'}

    inp = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']

    out = ['our language is impossible to understand' ,'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']

    for ind_in, i in enumerate(inp):
        for ind, c in enumerate(i):
            mapping[c] = out[ind_in][ind]
            
    output = ''
    
    for n in string:
        output += mapping[n]
        
    return output
    
if __name__ == "__main__":
    f = open('test.in','r').read().split('\n');
    num_tests = f.pop(0)
    f_out = open('test.out', 'w')
    for i in range(int(num_tests)):
        if f[i] != '':
            f_out.write("Case #" + str(i+1) + ": " + google_translate(f[i]) + '\n')
            
    f_out.write('\n')
