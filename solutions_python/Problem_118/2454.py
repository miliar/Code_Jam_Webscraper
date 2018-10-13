from math import sqrt, ceil, floor
def  main(infile, outfile):
    f= open(infile)
    fout = open(outfile, 'wb')
    num=int(f.next())
    for num, line in enumerate(f):
        case = 'Case #'+str(num+1)+": "
        boundary= [int(num) for num in line.strip().split()]
        left, right= [int(ceil(sqrt(num))) for num in boundary]
        
        if right*right == boundary[1]:
            right +=1
        
        count = 0
        for root in range(left, right):
            square = str(root*root)
            if ispalindrome(square) and ispalindrome(str(root)):
                count+=1
                print square,  root
        print case+str(count)
        fout.write(case+str(count)+"\n")
    fout.close()
    
def ispalindrome(str):
    return ''.join(reversed(str)) ==str
            
        
if __name__ == "__main__":
    main("C-small-attempt1.in", 'fair.txt')
    print 'success'
