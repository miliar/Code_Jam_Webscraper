input = open('A-large.in','r');
output = open('output.txt','w');

nrTestCases = int(input.readline());

line = input.readline().strip('\n');
case = 1;
while line != '':
    print "Case #%d" % case
    values = line.split(' ');
    rows = int(values[0])
    columns = int(values[1])
    image = [];
    print "Example contains %d rows and %d columns" % (rows, columns);
    for i in range(rows):
        row = input.readline().strip('\n');
        imageRow = []
        for j in range(columns):
            imageRow.append(row[j])
        image.append(imageRow);
    
    impossible = False;
    for i in range(rows):
        for j in range(columns):
            
            if image[i][j] == '#':
                # check if we can replace
                if i + 1 < rows and j + 1 < columns:
                    if image[i][j + 1] == '#' and image[i + 1][j] == '#' and image[i + 1][j + 1] == '#':
                        # replace
                        image[i][j] = '/'
                        image[i][j + 1] = "\\"
                        image[i + 1][j] = "\\"
                        image[i + 1][j + 1] = '/'
                    else:
                        impossible = True;
                        break;
                else:
                    impossible = True;
        
        if impossible:
            break;
    
    output.write("Case #%d:\n" % case)
    if impossible:
        output.write("Impossible\n")
    else:
        for i in range(rows):
            row = ''
            for j in range(columns):
                row += image[i][j];
            output.write(row + '\n')

    print "Case done";
    
    case += 1;
    line = input.readline().strip('\n');
