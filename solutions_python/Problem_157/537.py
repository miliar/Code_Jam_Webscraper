import sys

mult_dict = { ('1','i'): 'i', ('1','1'): '1', ('1','j'):'j', ('1','k'):'k',
              ('-1','-i'): 'i', ('-1','-1'): '1', ('-1','-j'):'j', ('-1','-k'):'k',
              ('-1','i'): '-i', ('-1','1'): '-1', ('-1','j'):'-j', ('-1','k'):'-k',
              ('1','-i'): '-i', ('1','-1'): '-1', ('1','-j'):'-j', ('1','-k'):'-k',
              
              ('i','1'):'i', ('i','i'): '-1', ('i','j'):'k', ('i','k'):'-j',
              ('-i','-1'):'i', ('-i','-i'): '-1', ('-i','-j'):'k', ('-i','-k'):'-j',
              ('-i','1'):'-i', ('-i','i'): '1', ('-i','j'):'-k', ('-i','k'):'j',
              ('i','-1'):'-i', ('i','-i'): '1', ('i','-j'):'-k', ('i','-k'):'j',

              ('j','1'):'j', ('j','i'):'-k', ('j','j'):'-1', ('j','k'):'i',
              ('-j','-1'):'j', ('-j','-i'):'-k', ('-j','-j'):'-1', ('-j','-k'):'i',
              ('-j','1'):'-j', ('-j','i'):'k', ('-j','j'):'1', ('-j','k'):'-i',
              ('j','-1'):'-j', ('j','-i'):'k', ('j','-j'):'1', ('j','-k'):'-i',

              ('k','1'):'k', ('k','i'):'j', ('k','j'):'-i', ('k','k'):'-1',
              ('-k','-1'):'k', ('-k','-i'):'j', ('-k','-j'):'-i', ('-k','-k'):'-1',
              ('-k','1'):'-k', ('-k','i'):'-j', ('-k','j'):'i', ('-k','k'):'1',
              ('k','-1'):'-k', ('k','-i'):'-j', ('k','-j'):'i', ('k','-k'):'1',
            }

# Possible sets are limited to 2^8

def calculate( i, j, str_data, store,L ):
    if i == j:
        return str_data[i%L]
    elif (i,j) in store:
        return store[ (i,j) ]
    else:
        #print "Calculating for ", (i,j)
        acc = str_data[(i)%L]
        for k in range(i+1,j+1):
            #print "Calculating %s and %s for %s"%((start,stop_1),(stop,stop),(start,stop))
            acc = mult_dict[(acc,str_data[k%L])]
            store[(i,k)] = acc
        return store[(i,j)]
    

def solve( L, X, str_data):
    total_length = l*x
    dct = {}
    sset = set(str_data)
    if calculate(0, total_length-1, str_data, dct, L ) != '-1':
        return "NO"
    elif len(sset) == 1:
        return "NO"

    for i in range(total_length-2):
        if calculate(0,i,str_data,dct,L) == 'i':
              for j in range(i+1, total_length-1):
                  if 'j' == calculate(i+1,j,str_data,dct,L):
                      #print "Checking: ", ((0,i),(i+1,j),(j+1,total_length-1))
                      if 'k' == calculate(j+1, total_length-1,str_data,dct,L):
                          return "YES"
    #print 'Store: ', dct
    return "NO"
    

with open(sys.argv[1]) as f:
    num_cases = int(f.readline().rstrip())
    case = 0
    while num_cases:
        num_cases -= 1
        case +=1
        l, x = [int(x) for x in f.readline().rstrip().split()]
        str_data = f.readline().rstrip()
        #print 'Data: ', data
        #print str_data, x
        print "Case #%d: %s" % (case, solve(l,x,str_data))

