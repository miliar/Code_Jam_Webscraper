dict = {'f':'c','g':'v','d':'s',' ':' ','e':'o','b':'h','c':'e','a':'y','n':'b','o':'k','l':'g','m':'l','j':'u','k':'i','h':'x','i':'d','w':'f','v':'p','u':'j','t':'w','s':'n','r':'t','q':'z','p':'r','z':'q','y':'a','x':'m','\n':''}
myInput=open("A-small-attempt0.in", "r");
myOutput = open("output.txt", "w+");
X = myInput.readline()
result='';
lines = int(X);
start = 2;
for index in range(0,lines):
        next_line = myInput.readline();        
        string =("Case #"+str(index+1)+": ");
        for i in range(0, len(next_line)):
                string+= dict[next_line[i]];
        result+=string+'\n'
myOutput.write(result)
myInput.close()
myOutput.close()
