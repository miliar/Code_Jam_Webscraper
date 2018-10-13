i1=1;
for x in range(int(raw_input())):
    n , k=map(int, raw_input().split());
    k1 =  int((n*2)/3);
    if (k ==1):
        if(n %2 ==0):
            print "Case #"+str(i1)+": " +str(int(n/2))+" "+str(int(n/2) -1);
        else:
            print "Case #"+str(i1)+": " +str(int((n-1)/2))+" "+str(int((n-1)/2));
    elif(k<=k1):
        state = [];
        state.append(1);
        for a in range(n):
            state.append(0);
        state.append(1);
        ##print state;
        ans =[];
        for l in range(k):
            points = dict();
            points[0] =[-10, -10];
            for a in range (1,n+1, 1):
                ls =0;
                rs =0;
                if(state[a] != 1):
                    i = a-1;
                    while(i>=0):
                        if(state[i] == 0):
                            ls = ls+1;
                        else:
                            break;
                        i = i-1;
                    i = a+1;
                    
                    while(i <= n+1):
                        if(state[i] == 0):
                            rs = rs+1;
                        else:
                            break;
                        i= i+1;
                else:
                    ls =-1;
                    rs=-1;
                points[a] = [ls, rs];
            ##print "points : " , points;
            far_cl = [];
            far_cl.append(-1);
            for a in range (1,n+1, 1):
                far_cl.append(min(points[a]));
            far_cl.append(-1);
            ##print "far_cl : " ,far_cl;
            max_points= max(far_cl);
            ##print "max_points : " ,max_points;
            count_max_points = far_cl.count(max_points);
            if (count_max_points >0):
                max_point_list=[];
                for u in range (count_max_points):
                    max_point_list = [i for i, x in enumerate(far_cl) if x ==max_points ]
                ##print "max_point_list : " , max_point_list;
                selected_stall_index =0;
                for p in max_point_list:
                    if(max(points[p]) > max(points[selected_stall_index])):
                        selected_stall_index = p;
            else:
                selected_stall_index = far_cl.index(max_points);
            state[selected_stall_index]=1;
            ans=points[selected_stall_index] 
            ##print selected_stall_index;
            ##print state;

        print "Case #"+str(i1)+": "+str(max(ans))+" "+str(min(ans));
    else:
        print "Case #"+str(i1)+": 0 0";
    i1 = i1+1;
