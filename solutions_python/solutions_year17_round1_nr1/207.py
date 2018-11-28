level = __file__.split("\\")[-1][0]
file_is_small = 0
attempt = 0
name = level+"-small-attempt"+str(attempt) if file_is_small else level+"-large"
input_file = file(name+".in","r")
output_file = file(name+"-output.txt","w")

def test_case():
    [R,C] = [int(x) for x in input_file.readline().split()]
    RC = []
    for i in xrange(R):
        RC.append([x for x in input_file.readline().strip()])
    initial = set()
    unset = '?'
    for r in xrange(R):
        for c in xrange(C):
            letter = RC[r][c]
            if(letter != unset and not letter in initial):
                initial.add(letter)
                
                right = c+1
                left = c-1
                while(left >= 0 and RC[r][left] == unset):
                    RC[r][left] = letter
                    left -= 1
                left += 1

                while(right < C and RC[r][right] == unset):
                    RC[r][right] = letter
                    right += 1
                right -= 1
                
                top = r+1
                bottom = r-1
                fill = True
                while(fill and top < R):
                    for i in xrange(left,right+1):
                        if(not RC[top][i] == unset):
                            fill = False                            
                    if(fill):
                        for i in xrange(left,right+1):
                            RC[top][i] = letter
                        top += 1

                fill = True
                while(fill and bottom >= 0 ):
                    for i in xrange(left,right+1):
                        if(not RC[bottom][i] == unset):
                            fill = False                            
                    if(fill):
                        for i in xrange(left,right+1):
                            RC[bottom][i] = letter
                        bottom -= 1
    return "\n" + "\n".join(["".join(line) for line in RC])

T = int(input_file.readline())
for test in xrange(T):
    out = "Case #{0}: {1}".format(test+1,test_case())
    #print out
    output_file.write(out + "\n")
    
input_file.close()
output_file.close()
