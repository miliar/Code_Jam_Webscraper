def solve(input_str):
    input_str_part = input_str.split()
    X = int(input_str_part[0])
    R = int(input_str_part[1])
    C = int(input_str_part[2])
    N = R * C #Number of grids
    if (R < C): #Choose the smaller and larger
        L = C
        S = R
    else:
        L = R
        S = C
    W = 0 #Win 0 for RICHARD, 1 for GABRIEL
    if (X < 7):
        if (N % X == 0):
            #Setting X-omino smaller and larger
            if (X <= L):
                X -= 1
                XS = 1 + X / 2 
                XL = 1 + (X + 1) / 2
                if (XS <= S and XL <= L):
                    W = 1
                    X += 1
                    if(X == 4):
                        if (S == 2):
                            W = 0
      
    
    if (W == 0):
        output = 'RICHARD'
    else:
        output = 'GABRIEL'
    return output

testcases = input()
    
for caseNr in xrange(1, testcases+1):
    cipher = raw_input()
    print("Case #%i: %s" % (caseNr, solve(cipher)))