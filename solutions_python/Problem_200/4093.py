
def main():
    with open("tidy_numbers.txt") as f:
        content = f.readlines()
        
    c = [x.strip() for x in content] 

    for i, case in enumerate(c[1:]):
        print "Case #" + str(i+1) + ":",
        tidy(case)
        


def tidy(case):
    n = list(case[::-1])
    n = map(int, n)

    for d in range(0, len(n)):
       
        if d+1 < len(n): 
            while  d + 1 < len(n) and n[d] < n[d+1]:                   
                num = int(''.join(map(str, n[::-1])))
                num -= 1
                n = list(str(num)[::-1])
                n = map(int, n)
            
    print int(''.join(map(str, n[::-1])))

    
    #print listToInt(n[::-1])


main()
