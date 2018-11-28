import numpy as np

# //////////////////////// PARSER /////////////////////////////

def getInfo(line):
    t = []
    for n in line.split(' '):
        t.append(int(n))
    return t

def parse(path):
    file = open(path,"r");
    nbCases = int(file.readline());
    txt = file.readlines();
    cases = []
    for line in txt:
        cases.append(line);
    file.close()
    return cases

# /////////////////////////// WORK //////////////////////////////

def work(t):
    counters = [0 for i in range(10)];
    liste = [['Z',"ZERO",0],['W',"TWO",2],['U',"FOUR",4],['X',"SIX",6],['G',"EIGHT",8],['O',"ONE",1],['F',"FIVE",5],['T',"THREE",3],['S',"SEVEN",7],['I',"NINE",9]];
    for i in range(10):
        char,chain, nb = liste[i];
        counter,t = delete(t,char,chain);
        counters[nb] = counter;
    rep = ""
    for i in range(10):
        for k in range(counters[i]):
            rep += str(i);
    return rep


def delete(word,c,chain):
    counter = 0;
    for i in word:
        if i == c:
            counter+=1;
    for char in chain:
        counter2 = counter;
        i = 0;
        while(counter2>0):
            if (word[i] == char):
                if i == 0:
                    word = word[1:];
                elif i == len(word)-1:
                    word = word[:i];
                else:
                    word = word[:i]+word[i+1:]
                counter2 = counter2 - 1;
            else:
                i+=1;
    return [counter,word];

# //////////////////// MAIN //////////////////////////////////

def createOutput(data,path):
    file = open(path,'w');
    for i in range(len(data)):
        R = work(data[i]);
        file.write("Case #"+str(i+1)+": "+R+"\n");
    file.close();

def main(txtInput,txtOutput):
    data = parse(txtInput);
    createOutput(data,txtOutput);
    

main("A-large.in","output.out");
