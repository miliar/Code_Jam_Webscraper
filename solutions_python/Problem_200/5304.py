import sys
        
def nonDecreasing(N):
    digits=list(map(int,str(N)))
    ll = len(digits)
    for i in range(1,ll):
        if digits[ll-1]<digits[ll-2]:
            return False
        digits.pop()
        ll-=1
            
    return True

def main():
    i=0
    for idx,line in enumerate(sys.stdin):
        if idx==0:
            num_case=int(line)
        else:
            i+=1
            case = int(line)
            while case>=1:
                if nonDecreasing(case):
                    print("Case #"+str(i)+": "+str(case))
                    break
                else:
                    case-=1
main()