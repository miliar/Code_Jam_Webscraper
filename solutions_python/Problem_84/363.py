import sys 

isprint = False 
#isprint = True 
def comment(t):
    if(isprint): print t

if __name__ == '__main__':
    data = open(sys.argv[1])
    n_case = int(data.readline().strip())
    for n in xrange(1,n_case+1):
        result = ""
        y_len, x_len = tuple( int(x) for x in data.readline().strip().split()) 
        pics = []
        for y in xrange(y_len):
            pics.append([x for x in data.readline().strip()]) 
        
        comment("pics : " + repr(pics))
        
        for y in xrange(y_len):
            for x in xrange(x_len):
                try:
                    if pics[y][x] == "#":
                        if pics[y][x] != ".":
                            pics[y][x] = "/"
                        else:
                            result = "Impossible" 
                            break
                        if pics[y][x+1] != ".":
                            pics[y][x+1] = "\\"
                        else:
                            result = "Impossible" 
                            break
                        if pics[y+1][x] != ".":
                            pics[y+1][x] = "\\"
                        else:
                            result = "Impossible" 
                            break
                        if pics[y+1][x+1] != ".":
                            pics[y+1][x+1] = "/"
                        else:
                            result = "Impossible" 
                            break
                        comment("pics : " + repr(pics))
                        #raw_input() 
                except:
                    result = "Impossible" 
                    break

        print "Case #%d:"%n
        if result == "Impossible": 
            print "Impossible"
        else:
            for line in pics:
                print "".join(line) 
