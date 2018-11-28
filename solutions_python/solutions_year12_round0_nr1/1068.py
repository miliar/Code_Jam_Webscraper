sample_inp = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

sample_outp = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

# reproduce mapping from sample input/output
mapping = {'a':'y', 'o': 'e', 'z':'q'}
for i in xrange(len(sample_inp)):
    mapping[sample_inp[i]] = sample_outp[i]

abc = list('abcdefghijklmnopqrstuvwxyz')
remaining_keys = filter(lambda c: not(c in mapping.keys()), abc)
remaining_values = filter(lambda c: not(c in mapping.values()), abc)
for (k,v) in zip(remaining_keys, remaining_values):
    mapping[k] = v

# get input file
inp_name = raw_input("What's the input file name?\n")
inp = open(inp_name)

# initialize output file
outp = open('output.out','w')

# get N
N_str = inp.readline().replace('\n','')
N = int(N_str)

# translate input
for i in xrange(1,N+1):
    line = inp.readline()
    translation = map(lambda c: mapping[c], line)
    result = 'Case #' + str(i) + ': ' + ''.join(translation)
    print result
    outp.write(result)

# close input/output files    
inp.close()
outp.close()
