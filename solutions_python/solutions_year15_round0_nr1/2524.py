def main():
    data = open("A-large.in", "r")
    
    output = open('result.out','w')
    
    num_of_cases = data.next()
    
    for i in xrange(1, int(num_of_cases) + 1):
        output.write('case #' + str(i) + ': ')
        
        line = data.next()
        
        res = line.split()
        
        t_max = res[0]
        
        audience = res[1]
        
        res = 0
        curr_aud = int(audience[0])
        
        for j in xrange(1, int(t_max) + 1):
            diff = j - curr_aud
            
            if diff > 0:
                res += diff
                curr_aud += diff
                
            curr_aud += int(audience[j])

            
        output.write(str(res) + '\n')
    

    data.close()
    output.close()




if __name__ == "__main__":
    main()