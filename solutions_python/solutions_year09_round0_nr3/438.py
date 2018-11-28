search_string = list("welcome to code jam");
def find_number(string, pos):
    global search_string;
    count = 0;
    if(pos>18):
        return 1;
    string=list(string);
    for i in range(0, len(string)):
        if(string[i]==search_string[pos]):
            count+=find_number(''.join(string[i:]), pos+1);
    return count;
fin = open("A-small.in");
fout = open("test.out", 'w');
cases = int(fin.readline()[:-1]);
for i in range(0, cases):
    temp = fin.readline()[:-1];#throws out the endline character and gets the string
    temp = str(find_number(temp, 0));
    while(len(temp)<4):
        temp = "0"+temp;
    
    fout.write("Case #"+str(i+1)+": "+temp+"\n");  

fout.close();
