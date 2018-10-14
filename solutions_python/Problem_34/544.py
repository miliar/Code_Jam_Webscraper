def finish_word(possibles, words):
    count = 0
    for i in range(0, len(words)):
        word = list(words[i]);
        pos = 0;
        good=True
        for char in word:
            if(char not in possibles[pos]):
                good=False
            pos+=1
        if(good==True):
            count+=1
    return count;
            
words = [];
fin = open("A-small.in");
fout = open("test.out", 'w');
nums = fin.readline();
nums = nums.split(' ');
num_chars = int(nums[0]);
num_words = int(nums[1]);
cases = int(nums[2][:-1]);
for i in range(0, num_words):
    a = fin.readline();
    a = a[:-1];
    words.append(a);
for i in range(0, cases):
    possible = []
    count = 0;
    temp = list(fin.readline());
    j=0;
    while(j<len(temp)):
        possible.append([]);
        if(temp[j]=='('):
            j+=1
            while(temp[j]!=')' and temp[j]!='\n'):
                possible[len(possible)-1].append(temp[j]);
                j+=1
        elif(temp[j]!='\n'):
            possible[len(possible)-1].append(temp[j]);
        else:
            possible = possible[:-1]
        j+=1
    temp = []
    count= finish_word(possible, words);
    fout.write("Case #"+str(i+1)+": "+str(count)+"\n");
    print i
fout.close();
