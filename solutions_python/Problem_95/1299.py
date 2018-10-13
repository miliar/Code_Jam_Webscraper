#!/usr/bin/python
import sys;

def translate(sentence):
  if(len(sentence)==0):
     return ""
  else:
    if sentence[0]== 'a':
            return 'y'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'b':
            return 'h'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'c':
            return 'e'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'd':
            return 's'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'e':
            return 'o'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'f':
            return 'c'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'g':
            return 'v'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'h':
            return 'x'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'i':
            return 'd'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'j':
            return 'u'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'k':
            return 'i'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'l':
            return 'g'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'm':
            return 'l'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'n':
            return 'b'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'o':
            return 'k'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'p':
            return 'r'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'q':
            return 'z'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'r':
            return 't'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 's':
            return 'n'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 't':
            return 'w'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'u':
            return 'j'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'v':
            return 'p'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'w':
            return 'f'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'x':
            return 'm'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'y':
            return 'a'+translate(sentence[1:len(sentence)]);
    elif sentence[0]== 'z':
            return 'q'+translate(sentence[1:len(sentence)]);
    else:
            return sentence[0]+translate(sentence[1:len(sentence)]);


lines=int(sys.stdin.readline());

for i in range(0,lines):
  sentence = sys.stdin.readline();
  translated= translate(sentence);
  sys.stdout.write("Case #"+str(i+1)+": "+translated);


