# input number of elements
# find elements-bit binary of all numbers from 1 to 2^elements-1
# if bit zero add to first list, if one add to second
# calculate xor_sum and sum_ of lists
# set sean_val  to 0 and max_diff to 0
# if xor_sums are equal and sum(sean_list)-sum(pat_list)>max_diff update sean_val
# if sean_val is 0 print NO else print sean_val

def binary(i,n):
    s = bin(i)[2:]
    if len(s)<n:
        padding = n-len(s)
        for i in range(padding):
            s = '0' + s
    return s

def xor(l):
    if (len(l) == 0):
        return 0
    elif len(l)==1:
        return l[0]
    else:
        res = l[0]
        for element in l[1:]:
            res = res ^ element
        return res

def main():
    f=open("inp.txt","r")
    op = open("output1.txt","w")
    t = int(f.readline())
    for case in range(1,t+1):
        n = int(f.readline())
        values = map(int,f.readline().split())
        sean_val = 0
        possible = False
        for i in range(1,2**n-1):
            b = binary(i,n)
            sean = []
            pat = []
            count=0
            for bit in b:
                if bit == '0':
                    sean.append(values[count])
                else:
                    pat.append(values[count])
                count+=1
            x_sean_sum = xor(sean)
            x_pat_sum = xor(pat)
        
            if (x_sean_sum == x_pat_sum):
                possible = True
                if (sum(sean)>sean_val):
                    sean_val = sum(sean)

        if not possible:
            op.write("Case #" + str(case) + ": NO"+'\n')
        else:
            op.write("Case #" + str(case) + ": " + str(sean_val)+'\n')
    f.close()
    op.close()

if __name__ =="__main__":
    main()

            
