import sys

def initialize():
    file_in = 'D:\code jam\input.txt'
    file_out = 'D:\code jam\output.txt'
    
    try:
        data_in  = open(file_in, 'r')
    except:
        print("Can't open file \'" + data_in +"\'")
        sys.exit()
    
    try:
        data_out  = open(file_out, 'w')
    except:
        print("Can't write to file \'" + data_out +"\'")
        sys.exit()

    return(data_in, data_out)

def get_variables():
    dictionary={}
    dictionary[' ']=' '
    dictionary['y']='a'
    dictionary['n']='b'
    dictionary['f']='c'
    dictionary['i']='d'
    dictionary['c']='e'
    dictionary['w']='f'
    dictionary['l']='g'
    dictionary['b']='h'
    dictionary['k']='i'
    dictionary['u']='j'
    dictionary['o']='k'
    dictionary['m']='l'
    dictionary['x']='m'
    dictionary['s']='n'
    dictionary['e']='o'
    dictionary['v']='p'
    dictionary['z']='q'
    dictionary['p']='r'
    dictionary['d']='s'
    dictionary['r']='t'
    dictionary['j']='u'
    dictionary['g']='v'
    dictionary['t']='w'
    dictionary['h']='x'
    dictionary['a']='y'
    dictionary['q']='z'


    G = str( data_in.readline() )
    G=G.rstrip()

    #print('G:', G)
    return(dictionary,G)

def calculate_result(dictionary,G):

    S=""
    for x in G:
        key = str(x)
        S = S + str(dictionary[key])
        #print('dictionary[key]', dictionary[key])
    
   
    
    #print('S:', S)
    #print('result:', j+1, k+1)
    #result = str(j+1) + ' ' + str(k+1)

    #Find index of each:
    #for x in current_items:
    #    result.append(P.index(x))
        
    return S
 
#help(["foo", "bar", "baz"])
    
(data_in, data_out) = initialize()
no_test_cases = int( data_in.readline() )

i = 0
while ( i < no_test_cases ):
    i+=1
    dictionary,G = get_variables()


    result = calculate_result(dictionary,G)
    print( 'Case #' + str(i) + ': ' + str(result) )
    data_out.write( 'Case #' + str(i) + ': ' + str(result) + '\n' )
    


