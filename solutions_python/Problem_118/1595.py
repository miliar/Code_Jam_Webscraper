f = open('/Users/michael/Dropbox/Coding/Code Jam/2013/fairandsquare/In.in')
f1 = open('/Users/michael/Dropbox/Coding/Code Jam/2013/fairandsquare/actualpalindromes.txt')
numcases = int(f.readline())
palindromes = []
palindrome = 0
while palindrome < 40: 
    palindromes.append(int(f1.readline().split()[0]))
    palindrome+=1
for a in range(numcases):
    print "Case #%d:" % (a+1),

    line = f.readline().split()
    low = int(line[0])
    high = int(line[1])
    result = 0
    for b in palindromes:
        if b >= low:
            if b<= high:
                result += 1
    print result
    
    
