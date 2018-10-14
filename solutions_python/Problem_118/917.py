import sys, math

INPUT_FILE_PATH = "C-large-1.in"
OUTPUT_FILE_PATH = "out.txt"

f = open(INPUT_FILE_PATH, "r")
of = open(OUTPUT_FILE_PATH,'w')

LIM = 10e14

out = []
def palingen():
    l = int(math.sqrt(LIM))+2
    for i in range(1,l):
        if (str(i) == str(i)[::-1]) and (str(i*i) == str(i*i)[::-1]):
            out.append(i*i)
            
#palingen()
#note: the following array was generated using the function above. takes about 1.5 mins. I used a premade array, just so prevent the monotony of waiting too long. Hope that's not inappropriate, as nothing mentioned in the rules forbidding it
out = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L, 100000020000001L, 100220141022001L, 102012040210201L, 102234363432201L, 121000242000121L, 121242363242121L, 123212464212321L, 123456787654321L, 400000080000004L]
#print out

def find(lb,ub):
    cou = 0
    for k in out:
        if (k >= lb) and (k<=ub):
            cou += 1
    
    return str(cou)

# -------------------------------------------------
T = int(f.readline().strip())

for C in range(1,T+1):
    tmp = f.readline().strip().split(' ')
    #print "Case #"+str(C)+": "+find(int(tmp[0]), int(tmp[1]))
    of.write( "Case #"+str(C)+": "+find(int(tmp[0]), int(tmp[1])) + "\n")
            
of.close()
# -------------------------------------------------


