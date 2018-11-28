from copy import copy

def get_count(new_art, a):
    return sum([el.count(a) for el in new_art])


def format_output(tiles):
    nr = []
    for r in tiles:
        nr.append("".join(r))
    tr_str = "\n".join(nr)
    tr_str = tr_str.replace('1','/')
    tr_str = tr_str.replace('2','\\')
    tr_str = tr_str.replace('3','\\')
    tr_str = tr_str.replace('4','/')
    return tr_str
    


def replace_numbers(new_art):
    for i,r in enumerate(new_art):
        for j,v in enumerate(r):
            if v == '1' or v == '3' :
                new_art[i][j] = '/'
            elif v == '2' or v == '4':
                new_art[i][j] = "b"
    return new_art
                
            


def edit_tiles():
    new_art = [list(el) for el in art]
    for i, r in enumerate(new_art):
        for j, c in enumerate(r):
            if new_art[i][j] != '#':
                continue
            if i>0 and new_art[i-1][j] == '1':
                new_art[i][j] = "3"
            elif i>0 and new_art[i-1][j] == '2':
                new_art[i][j] = '4'
            elif j>0 and new_art[i][j-1] == '1':
                new_art[i][j] = '2'
            else:
                new_art[i][j] = '1'
    if get_count(new_art,'1') == get_count(new_art,'2') == get_count(new_art, '3') == get_count(new_art, '4'):
        
        return format_output(new_art)
    else:
        return 'Impossible'
    
                
    

def test_cases():
    with open("in2.txt") as f:
        size = int(f.readline())
        #print 'size=%s'%size
        for i in range(size):
            global rows, columns
            rows, columns = [int(el) for el in f.readline().split()]
            #print rows, columns
            global art
            art = []
            for j in range(rows):
                art.append(f.readline().strip())
            print "Case #%s:"%(i+1)
            print "%s"%edit_tiles()

test_cases()
#print get_win_percentage('.11.')