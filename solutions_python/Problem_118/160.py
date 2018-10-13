import time

def build_fns_array2(symbols): # using the patterns of palindrome square roots of palindromes
    arr=[1,4,9]
    power=2
    for sqrt_digits in range(2,(symbols+1)/2):
        arr.append(int('1' + '0'*(sqrt_digits-2) + '1')**power) # 1000...0001
        arr.append(int('2' + '0'*(sqrt_digits-2) + '2')**power) # 2000...0002
        if sqrt_digits%2==0: # even numbers
            hd = (sqrt_digits-2)/2 # half digits, 4 here: 1 0001 1000 1
            for d in range(1,2**hd):
                b = bin(d+2**hd)[3:]
                if b.count('1')<=3:
                    arr.append(int('1' + b + b[::-1] + '1')**power) # 10111101
        else: # odd numbers
            hd = (sqrt_digits-2)/2 # half digits, 4 here: 1 0001 1 1000 1
            for d in range(1,2**hd):
                b = bin(d+2**hd)[3:]
                if b.count('1')<=3:
                    arr.append(int('1' + b +'0' + b[::-1] + '1')**power) # 1 011 0 110 1
                    arr.append(int('1' + b +'1' + b[::-1] + '1')**power) # 1 011 1 110 1
            for sh in range(hd):
                b = '0'*(hd-sh-1) + '1' + '0'*(sh)
                arr.append(int('1' + b +'2' + b[::-1] + '1')**power) # 1 001 2 100 1
            arr.append(int('1' + '0'*(sqrt_digits/2-1) + '1' + '0'*(sqrt_digits/2-1) + '1')**power) # 10...010...01
            arr.append(int('1' + '0'*(sqrt_digits/2-1) + '2' + '0'*(sqrt_digits/2-1) + '1')**power) # 10...020...01
            arr.append(int('2' + '0'*(sqrt_digits/2-1) + '1' + '0'*(sqrt_digits/2-1) + '2')**power) # 20...010...02
    arr.sort()
    return arr
    
def count_fns(arr,A,B):
    return [i>=A and i <=B for i in arr].count(True)

def main():     
    start_time = time.time()
##    f = open("in.txt")
    f = open("C-large-2.in")
    ff = open("out.txt", "w")
    N = int(f.readline())
    ins = []
    for i in range(N):
        ins.append(f.readline().replace("\n", "").split(" "))
    ins = [[int(col) for col in row] for row in ins] 

    arr = build_fns_array2(101)
    
    print "time: " + str(round(time.time()-start_time,2)) + "s"

    c=1
    for i in ins:
        sol = str(count_fns(arr, i[0], i[1]))
##        print "Case #" + str(c) + ": " + sol
        ff.write("Case #" + str(c) + ": " + sol + "\n")
        c+=1

    print "time: " + str(round(time.time()-start_time,2)) + "s"
    f.close()
    ff.close()

main()

