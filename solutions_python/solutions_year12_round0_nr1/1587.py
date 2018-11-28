inp = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv'];
outp = ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up'];

dct = {};

for i in range(3):
    for j in range(len(inp[i])):
        dct[inp[i][j]] = outp[i][j];

dct['q'] = 'z';
dct['z'] = 'q';
dct['\n'] = '\n';

f_in = open('A-small.in','r');
f_out = open('A-small.out.txt','w');

T = int(f_in.readline());

for t in range(T):
    inp_str = f_in.readline();
    f_out.write('Case #'+str(t+1)+': ');
    outp_str = '';
    for l in range(len(inp_str)):
        outp_str += dct[inp_str[l]];
    f_out.write(outp_str);

f_in.close();
f_out.close();
