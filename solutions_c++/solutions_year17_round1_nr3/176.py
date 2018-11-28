#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int t;

int ad,hd,ak,hk;
int b,d;
int n,m;
int ans;
int main()
{
    int i,j,k,times;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("ansC.out","w",stdout);
    
    cin>>t;
    
    for(times=1;times<=t;times++)
    {
        cin>>hd>>ad>>hk>>ak>>b>>d;
        
        m=n=0;
        if(d!=0)
        {
            n=ak/d;
            if(ak%d!=0)n++;
        }
        
        if(b!=0)
        {
            m=(hk-ad)/b;
            if((hk-ad)%b!=0)m++;
        }
        
        ans=0x3f3f3f3f;
        for(i=0;i<=n;i++)
        {
            for(j=0;j<=m;j++)
            {
                int r1,r2;
                r1=i;r2=j;
                int tt=0;
                int thd,tad,thk,tak;
                thd=hd;
                tad=ad;
                thk=hk;
                tak=ak;
                
                //cout<<r1<<' '<<r2<<"  !!!"<<endl;
                
                while(thk>0 && thd>0)
                {
                    tt++;
                    
                    int die=0;
                    if(r1>0)
                    {
                        die=(thd<=tak-d);
                    }
                    else if(r2>0)
                    {
                        die=(thd<=tak);
                    }
                    else
                    {
                        die=(thd<=tak && thk>tad);
                    }
                    
                    if(thd==hd-tak)
                    {
                        die=0;
                    }
                    
                    
                    if(die==1)
                    {
                        thd=hd;
                        thd-=tak;
                    }
                    else
                    {
                        if(r1>0)
                        {
                            tak=max(0,tak-d);
                            r1--;
                            thd-=tak;
                        }
                        else if(r2>0)
                        {
                            tad+=b;
                            r2--;
                            thd-=tak;
                        }
                        else
                        {
                            thk-=tad;
                            if(thk>0)
                            {
                                thd-=tak;
                            }
                        }
                    }
                    
                    //cout<<thd<<' '<<tad<<"   "<<thk<<' '<<tak<<endl;
                }
                
                if(thd>0 && thk<=0)
                {
                    ans=min(ans,tt);
                }
            }
        }
        if(ans!=0x3f3f3f3f)
        {
            cout<<"Case #"<<times<<": "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<times<<": IMPOSSIBLE"<<endl;
        }
        
    }
    
    
    
    
    return 0;
}
