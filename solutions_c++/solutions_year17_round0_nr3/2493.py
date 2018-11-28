#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;

ll ki;



int main()
{
     freopen("C-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    unsigned long long t,ti,n,k,i,j,l,done,m,pc,mn,mx,s;
    int flag;
    scanf("%llu",&t);
    for(ti=1; ti<=t; ++ti)
    {
        flag=0;
        done=1;
        pc=2;
        scanf("%llu %llu",&n,&k);
        ki=k-done;
        if(k > 1)
        {
            while(1)
            {
                m=n-done;
               // printf("m = %llu, pc = %llu\n",m,pc);
                if(pc>=m)
                {
                    flag=1;
                    break;
                }
                if(pc*2>=m)
                {
                    flag=2;
                    break;
                }
                if(pc*3>m)
                {
                    flag=3;
                    break;
                }
                done+=pc;
                if(done>=k)
                    break;
                ki=k-done;

                pc*=2;
            }


            if(flag==0)
            {

                if(m%pc==0)
                {
                    mn=((m/pc)-1)/2;
                    mx=(m/pc)/2;
                }
                else
                {
                    l=m%pc;
                    s=pc-l;

                    if(ki<=l)
                    {
                        mx=((m/pc)+1)/2;
                        mn=(m/pc)/2;
                    }
                    else
                    {
                        mn=((m/pc)-1)/2;
                        mx=(m/pc)/2;
                    }


                }
            }
            else
            {
                if(flag==1)
                    mx=mn=0;
                if(flag==2)
                {
                    j=m%pc;
                    if(ki<=j)
                        mx=1,mn=0;
                    else if(j==0 && ki<=(m/pc))
                        mx=1,mn=0;
                    else
                        mx=mn=0;
                }
                if(flag==3)
                {
                    j=m%pc;
                    if(ki<=j)
                        mx=mn=1;
                    else
                    {
                        ki-=j;
                        pc+=j;
                        m-=j;
                        j=m%pc;
                        if(ki<=j)
                            mx=1,mn=0;
                        else if(j==0 && ki<=(m/pc))
                            mx=1,mn=0;
                        else
                            mx=mn=0;


                    }
                }
            }
        }
        else
        {
            mn=(n-1)/2;
            mx=n/2;
        }
        printf("Case #%llu: %llu %llu\n",ti,mx,mn);
    }
    return 0;
}
