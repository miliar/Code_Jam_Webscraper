# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 05:55:08 2012

@author: Elite
"""

import sets;
        
debug = False;

samplesEncoded = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"];

samplesDecoded = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"];

alpha = "abcdefghijklmnopqrstuvwxyz";
cipher = {'a':'y', 'o':'e', 'z':'q'};

for i in range(len(samplesEncoded)):
    encoded = samplesEncoded[i];
    decoded = samplesDecoded[i];
    for j in range(len(encoded)):
        cipher[encoded[j]] = decoded[j];
        
for letter in alpha:
    if not letter in cipher:
        cipher[letter] = 'z';
        break;   
        
        
if debug: print "Generated cipher: " + str(cipher);   

def decodeString(s):
    decodedChars = [];
    for letter in s:
        decodedChars.append(cipher[letter]);
    return ''.join(decodedChars);

inFile = open("A-small-attempt0.in");
outFile = open("A-small-attempt0.out", "w");

numTests = int(inFile.readline());

for testNum in range(numTests):
    testCase = inFile.readline().rstrip("\n");
    
    decodedTest = decodeString(testCase);
                                        
    if debug: print testCase;          
    if debug: print decodedTest;
    outFile.write("Case #" + str(testNum+1) + ": " + decodedTest + "\n");

inFile.close();
outFile.close();