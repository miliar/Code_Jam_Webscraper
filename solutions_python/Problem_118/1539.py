from math import sqrt

def digits(n):
    r=[]
    i=n;
    while i>0:
        r.append(i%10)
        i=i//10
    return r

def palindrome(li):
    if len(li)==1 or len(li)==0:
        return True
    else:
        return (li[0]==li[-1]) and palindrome(li[1:-1])

def squares(low,high):
    i=int(sqrt(low))
    if i*i<low:
        i=i+1    #trying to avoid floating point weirdness
    sq=i*i
    while sq<=high:
        yield sq
        i=i+1
        sq=i*i

def ans(li,low,high):
    return len([i for i in li if i>=low if i<=high])

if __name__=='__main__':
    fs=[i for i in squares(1,10**14) if palindrome(digits(i)) if palindrome(digits(round(sqrt(i))))] #find ONCE
    trials=int(input())
    for i in range(trials):
        low,high=(int (e) for e in input().split())
        print("Case #"+str(i+1)+": "+str(ans(fs,low,high)))
