f_in = open('B-large.in','r');
f_out = open('B-large.out.txt','w');

T = int(f_in.readline());

for t in range(T):
    inp_str = f_in.readline();
    inp_lst = inp_str.split(' ');
    N = int(inp_lst[0]);
    S = int(inp_lst[1]);
    p = int(inp_lst[2]);

    easy_cases = 0;
    border_cases = 0;
    
    for i in range(N):
        score = int(inp_lst[3+i]);
        if (score >= 3*p - 2):
            easy_cases += 1;
        elif (score >= max(1,3*p - 4) ):
            border_cases += 1;

    all_cases = easy_cases + min(S,border_cases);
    
    f_out.write('Case #'+str(t+1)+': '+str(all_cases)+'\n');

f_in.close();
f_out.close();
