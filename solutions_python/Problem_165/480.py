import sys

class InvalidException(Exception):
    pass

args = sys.argv

def solve(R, C, W):
    if W == 1:
        return str(int(R * C))
    elif C == W and R < C:
        return str(W)
    elif R == W and C < R:
        return str(W)
    elif R == 1 or C == 1:
        X = R
        if R == 1:
            X = C
            C = 1
        NO = X + 1 - W
        res = 0
        """if X % 2 == 0:
            return str((int((X-1)/W) + W))
        else:
            return str((int(X/W) + W))"""
        Wt = W
        while NO > 1:
            tr = min(Wt, NO - 1)
            res = res + 1
            if Wt >= NO - 1 and (NO - 1) > NO/2:
                W = W - 1
                NO = NO - 1
            else:
                NO = NO - tr
        res = res + W
        return str(res)
        

if len(args) == 2:
    f = open(args[1],'r')
    of = open('output.txt','w')
    breakFlag = False
    num = 0
    numCalculated = False
    i = -1
    while not breakFlag:
        l = f.readline()
        if not numCalculated:
            num = int(l.strip())
            numCalculated = True
            i = 0
        elif i < num:
            ls = l.strip().split(' ')
            R , C , W = int(ls[0]) , int(ls[1]) , int(ls[2])
            try:
                result = solve(R , C , W)
            except InvalidException:
                result = ''
            of.write('Case #'+str(i+1)+': ' + str(result) + '\n')
            print('Case #'+str(i+1)+': ' + str(result))
            i = i + 1
        else:
            breakFlag = True
    of.flush()
    of.close()
    f.close()

sys.exit()


"""of.write('Case #'+str(i+1)+': NO\n')
print('Case #'+str(i+1)+': NO')"""
