def isTidy(n):
    if n < 10:
        return True
    
    l = list(str(n))
    numIsTidy = True
    
    for a, b in zip(l, l[1:]):
#        print("({}, {})".format(a[0], b[0]))
        if a > b:
            numIsTidy = False
            break
    
    return numIsTidy

#with open('problemB.txt', 'r') as f:
#with open('B-small-attempt0.in', 'r') as f:
#with open('B-small-attempt1.in', 'r') as f:
with open('B-large.in', 'r') as f:
    content = f.read().splitlines()
    
content = list(reversed(content))
numTestCases = int(content.pop())

# for each test          
for i in range(1, numTestCases+1):
    n = int(content.pop())
    
    # brute force case, won't work for the large case where n<1e18
    #    while not isTidy(n):
    #        n = n - 1
        
    # smarter, faster case
    while not isTidy(n):
        # find the offending digit
        digits = list(str(n))
        for index, value in enumerate(digits):
            # if tidy-ness is violated
            if digits[index] > digits[index+1]:
                # if violated by the first digit, zero out other digits and subtract 1
                if index == 0:
                    digits[1:] = (len(digits) - 1) * ['0']
                    n = int(''.join(digits)) - 1 
                    break
                # otherwise, decrement the offending digit until it no longer violate tidy-ness
                # and set other digits to 9
                else:
                    digits[index] = str(int(value)-1)
                    digits[index+1:] = (len(digits) - index - 1) * ['9']
                    n = int(''.join(digits))
                    break

    # output solution
    print("Case #{}: {}".format(i, n))