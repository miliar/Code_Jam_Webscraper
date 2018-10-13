'''
Created on 2010/05/08

@author: banana
'''

if __name__ == '__main__':
    pass

fp = open("B-large.in", "r")

lines = fp.readlines()

T = int(lines[0])

fpout = open("B-large.txt", "w")

for t in range(1, T+1):
    line = lines[t].split()
    
    C = int(line[0])
    compo_list = []
    for i in range(C):
        s = line[i+1]
        compo_list.append( (s[0], s[1], s[2])  )
    D = int(line[C+1])
    oppo_list = []
    for i in range(D):
        s = line[i+C+2]
        oppo_list.append( (s[0], s[1])  )   
    
    invoke_list = line[C+D+3]
    
    cur_list = []
    for ch in invoke_list:
        cur_list.append(ch)
        loop_flg = True
        #composite
        while loop_flg:
            if len(cur_list) < 2:
                loop_flg = False
            else :
                tail = (cur_list[-2], cur_list[-1])
                loop_flg = False
                # match
                for (x,y,z) in compo_list:
                    if (x == tail[0] and y == tail[1]) or ( x == tail[1] and y == tail[0]):
                        cur_list.pop()
                        cur_list.pop()
                        cur_list.append(z)
                        loop_flg = True
                        break
         
        # oppose
        for (x,y) in oppo_list:
            if x in cur_list and y in cur_list:
                cur_list = []

    fpout.write("Case #%d: ["%(t))
    for i,x in enumerate(cur_list):
        fpout.write("%s"% x)
        if i < len(cur_list) -1:
            fpout.write(", ")
    fpout.write("]\n")    
        
        
fpout.close()