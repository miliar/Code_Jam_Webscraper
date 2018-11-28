f = open('input.txt','r')
tc = f.readline()

def stdOvation(shyMax, audience):
   aud = 0
   addAud = 0
   for idx, c in enumerate(audience):
         if (int(c) > 0 and aud+addAud < idx):
            addAud = idx - aud
         aud += int(c)
         if (aud+addAud) >= shyMax:
            return addAud

output = open('output.txt','w')
for x in xrange(1,int(tc)+1):
   tokens = f.readline().split() 
   audCnt = stdOvation(int(tokens[0]),tokens[1])
   line = "Case #{0}: {1}\n".format(x,audCnt)
   output.write(line)
