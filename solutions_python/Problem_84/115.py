fin = open("A-large.in")
fout = open("A-large.out", "wt")

def output(string):
    print string
    fout.write(string)
    
    
numCases = int(fin.readline().strip())
for caseIndex in range(1,numCases+1):
    # Code comes here
    nums = fin.readline().strip().split(" ")
    rows = int(nums[0])
    cols = int(nums[1])
    img = []
    for y in range (0,rows):
        line = fin.readline().strip()
        tmp = []
        for ch in line:
            tmp.append(ch)
        img.append(tmp)

    #print img
    possible = True
    for y in range(1, rows):
        for x in range(1,cols):
            if img[y-1][x-1]=='#' and img[y-1][x]=='#' and img[y][x-1]=='#' and img[y][x]=='#':
                img[y-1][x-1]='/'
                img[y-1][x]  ='\\'
                img[y][x-1]  ='\\'
                img[y][x]    ='/'
    for y in range(0,rows):
        for x in range (0,cols):
            if img[y][x]=='#':
                possible = False
                break
            
    output("Case #%d:\n" % caseIndex)
    if not possible:
        output("Impossible\n")
    else:
        for y in range (0,rows):
            s = "".join(img[y]) + "\n"
            output(s)
        
fin.close()
fout.close()
