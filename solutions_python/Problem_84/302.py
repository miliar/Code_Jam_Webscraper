# developped under python3.2

# test_file_name = 'A-test'
# test_file_name = 'A-small-attempt1'
test_file_name = 'A-large'
f = open(test_file_name + '.in', 'r')
fw = open(test_file_name + '.out', 'w')
T = int(f.readline())
for case in range(1,T+1):
    #print(i)
    
    line = f.readline()
    line = line.split()
    line.reverse()

    # count of elements
    R = int(line.pop())
    C = int(line.pop())

    # read data
    pic = [];

    for r in range(0,R):
        line = f.readline()
        line = list(line)
        line.reverse()

        pic_line = []
        for c in range(0,C):
            pic_line.append( line.pop() )

        pic.append( pic_line )
    # end read data

    # data process
    try:
        for r in range(0,R):
            for c in range(0,C):
                if( pic[r][c] == '#' ):
                    pic[r][c] = '/'
                    if( pic[r][c+1] == '#' and pic[r+1][c] == '#' and pic[r+1][c+1] == '#' ):
                        pic[r][c+1] = '\\'
                        pic[r+1][c] = '\\'
                        pic[r+1][c+1] = '/'
                    else:
                        raise Exception("error")                
        ans = ""
        for r in range(0,R):
            for c in range(0,C):
                ans += pic[r][c]
            ans+='\n'
        if(ans[-1] == '\n'):
            ans = ans[0:-1]
    except Exception:
        ans = "Impossible"
                    
            
    # end data process

    # result representation
#     ans = pic
    
    #print(ans)
    output = 'Case #' + str(case) +': \n' + str(ans)+'\n'
    print(output)

    fw.write(output)

    # end result representation

f.close()
fw.close()
