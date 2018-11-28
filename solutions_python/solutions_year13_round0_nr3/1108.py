import math
def palindrome(n):
    cn = n
    ni = 0
    while cn:
        ni=ni*10+cn%10
        cn=cn//10
    return n == ni
def main():
    fout = open("fair_and_square.out",'w')
    with open("fair_and_square.in",'r') as fin:
        case_numbers = int(fin.readline().strip())
        for i in range(case_numbers):
            a,b =  map(int,fin.readline().strip().split())
            k = 0
            q = int(math.ceil(math.sqrt(a)))
            end = int(math.floor(math.sqrt(b)))
            while(q<=end):
                if palindrome(q) and palindrome(q*q):
                    k+=1
                q+=1
            fout.write("Case #{}: {}\n".format(i+1,k))



if __name__ == '__main__':
    main()
