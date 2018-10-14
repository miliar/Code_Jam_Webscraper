__author__ = 'Sirna'


def meth1(size,inputs):
    maxdiff = 0
    ans = 0
    for i in range(size-1):
        if (inputs[i+1] < inputs[i]):
            diff = inputs[i] - inputs[i+1]
            ans+= diff
            if(diff>maxdiff):
                maxdiff = diff
    return ans,maxdiff

def meth2(size,inputs,maxdiff):
    ans = 0
    for i in range(size-1):
        if(inputs[i+1] <= inputs[i]):
            ans += min(maxdiff,inputs[i])
        else:
            ans += min(maxdiff,inputs[i])
    return ans

o = open("d.out","w")
if __name__ == "__main__":
    cases = input()

    for i in range(cases):
        time = input()
        inputs  = map(int,raw_input().split())

        ans,maxdiff = meth1(time,inputs)

        ans2 = meth2(time,inputs,maxdiff)
        o.write("Case #"+str((i+1))+": "+str(ans)+" "+str(ans2)+"\n")
    o.close()
