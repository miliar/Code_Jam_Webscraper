

def main():
    testcases = int(input())
    for caseNr in range(1, testcases+1):
        s,sn = input().split()
        n = int(sn)
        print("Case #%i: %i" % (caseNr, len(fltr(substr(s),n))))

def substr(s):
    j=1
    a=[]
    while True:
        for i in range(len(s)-j+1):
            a.append(s[i:i+j])
        if j==len(s):
            break
        j+=1
        #string=string[1:]
    return a

def sequence_consonant(s,n):
    i=0
    for c in s:
        if ( c=='a' or c=='e' or c=='i' or c=='o' or c=='u' ):
            i=0
        else:
            i+=1
            if i >= n:
                return True
    return False

def fltr(ls,n):
    nls=[]
    for s in ls:
        if sequence_consonant(s,n):
            nls.append(s)
    return nls

if __name__ == "__main__":
  main()
