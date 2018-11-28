T = 0
contents_list = []
out_f = open('results','w');

out_results = ("Draw","X won","O won","Game has not completed")

#  row and column sum only 0 or 2 , and no number 1
# ([0,0,0,0], [0,0,0,0,2], [0,0,2,0], [0,2,0,0], [2,0,0,0])
# column and row sum only 4(no include zero) or 5 (same as 4)
# ('1111', '1112', '1121', '1211', '2111')

#
# return value:
# 0 : no match
# 1 : x win
# 2 : o win

def check_atom(list_atom):
    if sum(list_atom) == 0 or sum(list_atom) == 2:
        if((1 in list_atom) != 1):
            return 1
    elif sum(list_atom) == 4 or sum(list_atom) == 5:
        if((0 in list_atom) != 1):
            return 2
    return 0

def check_row(list_c):
    value = 0
    for l in list_c:
        value = check_atom(l)
        if value != 0:
            return value
        else:
            continue

    return 0

def check_cols(list_c):
    _tmp = []
    for x in xrange(len(list_c)):
        _tmp.append([list_c[0][x],list_c[1][x],list_c[2][x],list_c[3][x]])
    return check_row(_tmp)

def check_diagonal_left(list_c):
    _tmp = []
    _tmp.append([list_c[0][0],list_c[1][1],list_c[2][2],list_c[3][3]])
    return check_atom(_tmp[0])

def check_diagonal_right(list_c):
    _tmp = []
    _tmp.append([list_c[0][3],list_c[1][2],list_c[2][1],list_c[3][0]])
    return check_atom(_tmp[0])

def checkLimits(c, p):
    if c <= 1000 and c >= 5:
        if p <= 1000 and p >= 1:
            return 1
    return 0

def check_complete(list_c):
    for x in list_c:
        if 3 in x:
            return 3
        else:
            return 0

# Print results to screen
def show(n,results):
    #print "Case #{}: {}".format(int(n+1),out_results[results])
    out_f.write("Case #{}: {} \n".format(int(n+1),out_results[results]))


# read files and return list of content
def readFile(file_name):
    f = open(file_name, 'r')
    nlist = [line.rstrip('\n') for line in f]
    f.close()
    return nlist

def cv_status(c):
    if(c=='X'):
        return 0
    elif(c=='O'):
        return 1
    elif(c=='T'):
        return 2
    else:
        return 3

def splitData(n,list_data):
    list_t = []

    for num in range(0,n*5,5):
        _tmp = []
        _tmp.append([cv_status(y) for y in list_data[num]])
        _tmp.append([cv_status(y) for y in list_data[num+1]])
        _tmp.append([cv_status(y) for y in list_data[num+2]])
        _tmp.append([cv_status(y) for y in list_data[num+3]])
        list_t.append(_tmp)

    return list_t


if __name__=="__main__":
# Default Valueable
    T = 0
    contents_list = []
# Get Data
    contents_list = readFile('A-small-attempt1.in')
    #contents_list = readFile('test.txt')
    T = int(contents_list.pop(0))
#
    test_list = splitData(T,contents_list)

    for x in xrange(T):
        val = check_row(test_list[x])
        if( val != 0):
            show(x,val)
            continue
        val = check_cols(test_list[x])
        if( val != 0):
            show(x,val)
            continue
        val = check_diagonal_left(test_list[x])
        if( val != 0):
            show(x,val)
            continue
        val = check_diagonal_right(test_list[x])
        if( val != 0):
            show(x,val)
            continue
        val = check_complete(test_list[x])
        if( val == 3):
            show(x,3)
            continue
        else:
            show(x,0)
            continue

out_f.close()
