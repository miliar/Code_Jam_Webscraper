#Brute Force first

def case():

    done=set()

    def solve(x):

        res=1
        done.add(x)

        new=x

        length=len(str(x))

        for i in xrange(length):

            if not new % 10:
                new=new/10
            else :
                new=new%10 * pow(10,length-1)+new/10

                if new in done: break

                if new>maxLimit or new<minLimit : continue

                res+=1
                done.add(new)

        return res

    def solveSingle():

        answers= ( solve(i) if not i in done else 0 for i in xrange(minLimit,maxLimit+1) )

        ans= sum( x*(x-1)/2 for x in answers )

        return ans

    minLimit,maxLimit=(int(x) for x in raw_input().split())

    return solveSingle()


n=int(raw_input())

for i in range(n):
    print 'Case #{}: {}'.format(i+1,case())
