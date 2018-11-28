#-*-coding: utf-8 -*-
import sys
f = open(sys.argv[1], 'r')
testcase = int(f.readline()[:-1])

dic = {" ":" ","y":"a","n":"b","f":"c","i":"d","c":"e","w":"f","l":"g","b":"h","k":"i","u":"j","o":"k","m":"l","x":"m","s":"n","e":"o","v":"p","z":"q","p":"r","d":"s","r":"t","j":"u","g":"v","t":"w","h":"x","a":"y","q":"z"}
for i in range(testcase):
    line = f.readline()[:-1]
    line_ed = ""
    for c in range(0, len(line)):
        line_ed += dic[line[c:c+1]]
    print("Case #%s: %s" %(i+1, line_ed))
