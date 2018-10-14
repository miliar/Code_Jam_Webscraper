def isPossible(field, N, M):
    for row in range(N):
        for column in range(M):
            n = column + M*row;
            height = field[n];
            #row
            if M != 1:
                row_vect = field[M*row:M*(row+1)];
                row_max = max(row_vect);
                if row_max > height:
                    #column
                    if N != 1:
                        col_vect = [];
                        for r in range(N):
                            col_vect.append(field[column + M*r]);
                        col_max = max(col_vect);
                        if col_max > height:
                            return "NO"
    return "YES"
    

fo = open("large_input.txt", "r")
fout = open("large_output.txt", "wb")

T = int(fo.readline());     # number of test cases

for i in range(T):
    sizestring = fo.readline()
    fieldsize = sizestring[0:len(sizestring)-1].split(" ");
    N = int(fieldsize[0]);
    M = int(fieldsize[1]);
        
    # read each line
    field = [];
    for j in range(N):
        string = fo.readline();
        field += string[0:len(string)-1].split(" ");
    for j in range(N*M):
        field[j] = int(field[j]);  
    
    result = isPossible(field,N,M);

    # Write to output
    output_str = "Case #" + str(i+1) + ": " + result + "\n";
    fout.write(output_str)

fo.close()
fout.close()

