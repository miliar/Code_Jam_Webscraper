from string import maketrans;
fob = open('c:/Users/Korisnik/Documents/python/Speaking in tongues/A-small-attempt0.in', 'r');
cases = int(fob.readline());
if cases <= 30 and cases >= 1:
    case = 1;
    output = [];
    while case <= cases:
        line = fob.readline();
        trans = maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq');
        output.append("Case #" + str(case) + ": " + line.translate(trans));
        case = case + 1;
    fob.close();
    fob = open('c:/Users/Korisnik/Documents/python/Speaking in tongues/output.txt', 'w');
    fob.writelines(output);
    fob.close();
else:
    print "Number of test cases must be >=1 and <=30.";
    fob.close();
    
