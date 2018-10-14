FILE_NAME = "C-small-attempt4.in"
f = open(FILE_NAME)
fout = open(FILE_NAME.split('.')[0]+'.out', 'w')
lines = int(f.readline().strip())

def palindrome(string):
    for index, char in enumerate(string[:len(string)//2]):
        if char != string[len(string)-index-1]:
            return False
        
    return True
    

for case, line in enumerate(f.readlines()):
    x,y = map(int, line.split())
    fair_squares = 0
    start = int(x**0.5)
    end = int(y**0.5)
    print(x,"to",y)
    for i in range(start, end+1):
        num = i**2
        if num >= x and num <= y and palindrome(str(num)) and palindrome(str(i)):
            fair_squares += 1
            print("fair and square:", num, i)

    fout.write("Case #{}: {}\n".format(case+1, fair_squares))
    print("Case #{}: {}".format(case+1, fair_squares))
    print()

f.close()
fout.close()

    
