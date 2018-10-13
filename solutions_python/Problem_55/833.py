def themePark(i , r ,k, q):
    #print i
    #print r
    #print k
    #print q
    count = 0
    while r >0:
        ride = 0
        temp = []
        while True:
            if peek(q) and (ride + peek(q) <= k):
                curr = pop(q)
                ride += curr
                temp.append(curr)
            else:
                count += ride
                for t in temp:
                    push(q,t)
                break
        r -= 1
    out = "Case #"+str(i)+": "+str(count)
    print out

def main():
    with open('C-small.in') as inputFile:
        cases = int(inputFile.next())
        i = 1
        temp = None
        for l in inputFile:
            ls = l.strip().split(' ')
            if i %2 == 0:
                themePark(i/2,int(temp[0]),int(temp[1]),map(int,ls))
            else:
                temp = ls
            i += 1

def push(q,item):
    q.append(item)

def pop(q):
    return q.pop(0)

def peek(q):
    try:
        return q[0]
    except:
        return None

main()
