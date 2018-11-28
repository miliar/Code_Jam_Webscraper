#!/usr/bin/python

strI="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

strO="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""


chars=set(strI);
print len(chars),sorted(list(chars));
chars=set(strO);
print len(chars),sorted(list(chars));

mapp = {'y':'a','e':'o','q':'z','z':'q'};


for i in xrange(len(strI)):
   inc = strI[i];
   ouc = strO[i];
   if inc in mapp:
      if ouc != mapp[inc]:print inc,ouc;
   else:
      mapp[inc]=ouc;

inF=open("A-small-attempt0.in");
outF=open("A-small-attempt0.out","w");
inF.readline();
i=1;
for line in inF:
   outF.write("Case #"+str(i)+": ");
   i+=1;
   for it in line:
      outF.write(mapp[it]);

inF.close();
outF.close();
