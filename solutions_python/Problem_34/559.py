#! /usr/bin/python

import sys, os, string;


file = sys.argv[1];

fp = open(file,"r");

line = fp.readline().rstrip();

[L, D, N] = line.split(' ');
L = int(L);
D = int(D);
N = int(N);

words = [];
for i in range(D):
    line = fp.readline().rstrip();
    words.append(line);
#print L, D, N;
#print words;


# test
for i in range(N):
    temp = words[:];
    #print temp;
    line = fp.readline().rstrip();
    #print line;
    j = 0;
    pos = 0;
    length = len(line);
    while j < length:
        letter = line[j];
        #print letter;
        if letter == '(':
            pattern = {};
            j = j + 1;
            letter = line[j];
            while letter != ')':
                pattern[letter] = 0;
                j = j + 1;
                letter = line[j];

     #       print pos, pattern;
            
            reserve = [];
            for word in temp:
     #            print word,
                 if not pattern.has_key(word[pos]):
      #               print "\t delete";
                     pass;
                 else:
                     reserve.append(word);
       #              print "\t reserv";
    
            temp = reserve[:];
        #    print temp;
            if len(temp) == 0:
                break;
            pos = pos + 1;
        else:
            reserve = []; 
         #   print pos,letter;
            for word in temp:
          #       print word,
                 if word[pos] != letter:
           #          print "\t delete";
                     pass;
                 else:
                     reserve.append(word);
            #         print "\t reserv";
    
            temp = reserve[:];
            #print temp;
            if len(temp) == 0:
                break;
            pos = pos + 1;
        j = j + 1;
        

    word_num = len(temp);
    print "Case #%d: %d" % (i + 1, word_num);
            
            
fp.close();
    
    
    
