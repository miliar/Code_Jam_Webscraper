import math

array = [];
with open("input.txt", "r") as ins:
    for line in ins:
        array.append(line);

numberOfTests = int(array[0]);

for i in range(1, numberOfTests+1):
    words = array[i].split();
    maxShy = int(words[0]);
    standing = 0;
    invitePepole = 0;
    level = 0;
    for c in words[1]:
        numOfPersons = int(c);
        if (standing >= maxShy):
            break;

        if (level == 0):
            standing += numOfPersons;
        else:
            if (numOfPersons != 0):
                newPepole = 0; 
                if (level > standing):
                    newPepole = level - standing;
                    invitePepole += newPepole;
                standing += numOfPersons + newPepole ;

        level+=1;

    with open('output.txt', 'a') as the_file:
        str1 = 'Case #' + str(i) + ': ' + str(invitePepole) + '\n';
        the_file.write(str1)


    
        
        
    
