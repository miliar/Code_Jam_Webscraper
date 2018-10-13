#peoblem A (magic Trick)
filename = "input.in"
file = open(filename, "r") 
lines = []
line1 = []
line2 = []
line3 = []
line4 = []
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def readFile():
    for line in file:
        lines.append(line)
        
def main():  
    readFile()
    count = 0
    T = int((file_len(filename)-1)/10) 
    for i in range(0,T):
        ans = 0
        g = eval(lines[i*10+1])
        line1 = lines[i*10+2].split() 
        line2= lines[i*10+3].split() 
        line3= lines[i*10+4].split() 
        line4= lines[i*10+5].split() 
        set1 = [line1,line2,line3,line4]
        g2 = eval(lines[i*10+6])
        line1 = lines[i*10+7].split() 
        line2= lines[i*10+8].split() 
        line3= lines[i*10+9].split() 
        line4= lines[i*10+10].split()    
        set2 = [line1,line2,line3,line4]
        print(g,set1,g2,set2,sep="\n")
        for j in range(4):
            print(set1[g][0], set1[g2][j])
            if set1[g][0] == set2[g2][j]:
                ans = (set1[g][0])
                count +=1
                break
        for j in range(4):
            print(set1[g][1], set1[g2][j])
            if set1[g][1] == set2[g2][j]:
                ans = (set1[g][1])
                count+=1
                break
        for j in range(4):
            print(set1[g][2], set1[g2][j])
            if set1[g][2] == set2[g2][j]:
                ans = (set1[g][2])
                count +=1
                break
        for j in range(4):
            print(set1[g][3], set1[g2][j])
            if set1[g][3] == set2[g2][j]:
                ans =(set1[g][3]) 
                count +=1
                break
        if ans == 0:
            ans = "Volunteer cheated!"
        if count > 1:
            ans = "Bad magician!" 
        print("Case #" + str(i+1) +":", ans)
        count  =0 
        ans = "n"

       


main()
   