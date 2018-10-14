'''
Created on 2017. 4. 8.

@author: Hyeonsu
'''
HAPPY_SIDE = "+"
BLANK_SIDE = "-"
HAPPY_PATTERN = ""
cnt = 0
flag = False

def flip(cakes, n, idx ):
    global cnt, flag
    # i is index of begins
    tg = cakes[idx:idx+n]
    HAPPY_PATTERN = ""
    for i in range( n ):
        HAPPY_PATTERN += HAPPY_SIDE

    if HAPPY_PATTERN == tg:
        print(tg)
        return cakes
        
    for i in range( len(tg) ):
        if tg[i]==HAPPY_SIDE : 
            tg = tg[:i]+BLANK_SIDE+tg[i+1:]
        else : 
            tg = tg[:i]+HAPPY_SIDE+tg[i+1:]
    cakes = cakes[:idx]+tg+cakes[idx+n:]
    #print(cakes,"(",tg,")")
    cnt+=1
    #print(cnt," ",cakes)
    return cakes

def pancake_flipper(line):
    global cnt, HAPPY_PATTERN, HAPPY_SIDE, BLANK_SIDE, flag
    vals=line.split(" ")
    cakes = vals[0]
    n = int(vals[1])
  #  cakes = "-++++++++-" 
  #  n = 2
#+-+-+-+ 3
#-++++++++- 3
    
    cnt = 0
    subStr = ""
    
    for i in range( n ):
        subStr += HAPPY_SIDE
    HAPPY_PATTERN = subStr
    
    idx = 0;
    loopCnt = 0
    while True:
        flag = False    
        if cakes == "+-+" : 
            return "IMPOSSIBLE"

        if idx > len(cakes)/2-1:
            idx=0

        if len(cakes)==n:
            if cakes == HAPPY_PATTERN:
                break
        elif len(cakes)<n:
            for i in range( len(cakes) ):
                if HAPPY_SIDE != cakes[i]:
                    return "IMPOSSIBLE"
            break
        if loopCnt>100:
            return "IMPOSSIBLE"
        
        if cakes[idx] != HAPPY_SIDE:
            cakes = flip( cakes, n, idx )
        if cakes[-idx-1] != HAPPY_SIDE:
            cakes = flip( cakes, n, len(cakes)-n-idx )

        if cakes[:n] == HAPPY_PATTERN:
            cakes = cakes[n:]
            flag = True 
        elif cakes[-n:] == HAPPY_PATTERN: 
            cakes = cakes[:-n]
            flag = True 
        
       # print(cakes)
       
        if flag == False:
            idx+=1
            loopCnt+=1
        else:
            idx =0
   
    return str(cnt)

if __name__ == '__main__':
    f = open("D:/Download/A-small-attempt10.in", 'r')
    n = int(f.readline())
    for i in range(n):
        print_str="Case #"+str(i+1)+": "
        line = f.readline()
        print_str += pancake_flipper(line)
        print(print_str)
    f.close()
    pass