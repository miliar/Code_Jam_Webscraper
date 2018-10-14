import sys

def main():
    t=int(sys.stdin.readline())
    for tests in range(t):
        arr=map(str,raw_input().split())
        actual=arr[1]
        people=0
        req=0
        
        for i in range(int(arr[0])+1):
            if people<i:
                req+=1
                people+=1
            people=people+int(actual[i])
        print "Case #"+str(tests+1)+": "+str(req)


main()
