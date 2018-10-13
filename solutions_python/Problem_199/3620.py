def flip(panSurf,left_minus,k):
    p_list = list(panSurf);
    for i in range(0,k):
        if(p_list[left_minus+i] == '-'):
            p_list[left_minus+i] = '+';
        else:
            p_list[left_minus+i] = '-';
    panSurf = "".join(p_list)
    return panSurf;


input_f = open('A-large.in' , 'r');
output_f = open('A_output.txt' , 'w');
T_s = input_f.readline();
T = int(float(T_s));

for i in range(1,T+1):
    s = input_f.readline();
    check = 0;
    raw = s.split();
    k = int(float(raw[1]));
    pan_surf = raw[0];
    flip_num = 0;
    left_minus = pan_surf.find('-');
    while(left_minus >= 0 & check == 0):
        if(len(pan_surf) - left_minus < k):
            check = 1;
            
            break;
        else:
            pan_surf = flip(pan_surf,left_minus,k);
            flip_num = flip_num + 1;
            left_minus = pan_surf.find('-');
    if(check == 1):
        out = 'Case #' + str(i) + ': ' + 'IMPOSSIBLE\n';
        output_f.write(out);
    else:
        out = 'Case #' + str(i) + ': ' + str(flip_num) + '\n';
        output_f.write(out);
            

output_f.close();
input_f.close();
