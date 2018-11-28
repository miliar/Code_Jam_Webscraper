ip=open('input.txt','r')
op=open('output.txt','w')
for i in range(int(ip.readline())):
    n,r,o,y,g,b,v=map(int,ip.readline().split())
    ans=''
    br=0
    while True:
        if r==0 and b==0 and y==0:
            if ans[0]==ans[-1]:
                br=1
                break
            else:
                break
        else:
            if ans=='':
                if max(r,b,y)==r:
                    ans+='R'
                    r-=1
                elif max(r,b,y)==b:
                    ans+='B'
                    b-=1
                else:
                    ans+='Y'
                    y-=1
            elif ans[-1]=='R':
                if y==0 and b==0:
                    br=1
                    break
                else:
                    if b==y:
                        if ans[0]=='B':
                            ans+='B'
                            b-=1
                        elif ans[0]=='Y':
                            ans+='Y'
                            y-=1
                        else:
                            ans+='Y'
                            y-=1
                    elif max(b,y)==b:
                        ans+='B'
                        b-=1
                    else:
                        ans+='Y'
                        y-=1
            elif ans[-1]=='B':
                if y==0 and r==0:
                    br=1
                    break
                else:
                    if r==y:
                        if ans[0]=='R':
                            ans+='R'
                            r-=1
                        elif ans[0]=='Y':
                            ans+='Y'
                            y-=1
                        else:
                            ans+='R'
                            r-=1
                    elif max(r,y)==r:
                        ans+='R'
                        r-=1
                    else:
                        ans+='Y'
                        y-=1
            elif ans[-1]=='Y':
                if r==0 and b==0:
                    br=1
                    break
                else:
                    if b==r:
                        if ans[0]=='B':
                            ans+='B'
                            b-=1
                        elif ans[0]=='R':
                            ans+='R'
                            r-=1
                        else:
                            ans+='B'
                            b-=1
                    elif max(b,r)==b:
                        ans+='B'
                        b-=1
                    else:
                        ans+='R'
                        r-=1
            else:
                pass
            #print(ans,r,b,y)
            
    if br==1:
        ans="IMPOSSIBLE"
    op.write("Case #"+str(i+1)+": "+ans+'\n')
                
ip.close()
op.close()
