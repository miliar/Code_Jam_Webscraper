 
 
map = {' ':' ', '\n':'\n','a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'} 
fin  =  open("A-small-attempt0.in","r")
fout = open("output.txt","a")
testCases = int(fin.readline())
case = 0
string = ""
if (testCases > 0 and testCases < 31):
    for line in fin:
        #print line
        case+=1
        string = "Case #" +str(case)+ ": " 
        #print "Case #",case,': ',
        for ch in line:
            try:
                tmp = map[ch]
                #print "word for  "+ ch+ " = " + tmp
            except KeyError:
                #print "key not found for ", ch, "sdfs"
                exit(1)
            string += tmp
            #print tmp,
        fout.write(string)
fout.close()   
            
    

     