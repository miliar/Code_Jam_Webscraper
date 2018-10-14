def alg(cmds):
    print(cmds)
    
    o_loc = 1
    o_time = 0
    b_loc = 1
    b_time = 0
    
    for i in range(len(cmds)/2):
        color = cmds[2*i]
        new_loc = int(cmds[2*i+1])
        print(str(color)+" "+str(new_loc))
        
        if color == 'O':
            dist = abs(new_loc - o_loc)
            o_time = max(b_time+1, o_time + dist + 1)
            o_loc = new_loc
        
        if color == 'B':
            dist = abs(new_loc - b_loc)
            b_time = max(o_time+1, b_time + dist + 1)
            b_loc = new_loc
            
    return [max(b_time, o_time)]

if __name__ == '__main__':
    fname = "A"
#    f = open(fname+".in.txt", "r")
    #f = open("/home/lawford/Desktop/"+fname+"-small-attempt0.in")
    f = open("/home/lawford/Desktop/"+fname+"-large.in")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
    piece1 = f.readline()
    while piece1 != '':
        result = alg(piece1.split(' ')[1:])
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
        piece1 = f.readline()

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.close()
    f.close()
