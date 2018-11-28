def solve(cipher): 
    inputs = cipher.split(" ") 
    Smax = inputs[0] 
    digits = inputs[1] 
    fcnt = 0 
    acnt = 0 
    #print digits 
    for i in range(len(digits)): 
        digit = int(digits[i]) 
        if digit==0:
            continue

        if (fcnt+acnt)<i:
            fcnt += (i-(acnt+fcnt)) 
        acnt += digit

    return str(fcnt) 
if __name__ == "__main__": 
    testcases = input() 
    for caseNr in xrange(1, testcases+1): 
        cipher = raw_input() 
        print("Case #%i: %s" % (caseNr, solve(cipher)))