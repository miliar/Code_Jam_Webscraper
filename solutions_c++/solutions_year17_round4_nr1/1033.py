#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

int n,p;
int g[111];
int t;
int ans;
int u[11];
int dp[111][111][111];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    int i,j,k,times;
    bool uu=0;
    int xx,yy;
    cin>>t;
    for(times=1;times<=t;times++)
    {
        cin>>n>>p;
        memset(u,0,sizeof(u));
        for(i=1;i<=n;i++)
        {
            cin>>g[i];
            u[g[i]%p]++;
        }
        uu=0;
        ans=1+u[0];
        if(p==2)
        {
            xx=u[1]/2;
            u[1]-=xx*2;
            ans+=xx;
        }
        else if(p==3)
        {
            xx=min(u[1],u[2]);
            u[1]-=xx;
            u[2]-=xx;
            ans+=xx;
            
            xx=u[1]/3;
            u[1]-=xx*3;
            ans+=xx;
            
            xx=u[2]/3;
            u[2]-=xx*3;
            ans+=xx;
        }
        else if(p==4)
        {
            int tmp=0;
            memset(dp,0,sizeof(dp));
            for(i=0;i<=u[1];i++)
            {
                for(j=0;j<=u[2];j++)
                {
                    for(k=0;k<=u[3];k++)
                    {
                        xx=dp[i][j][k];
                        
                        dp[i+4][j][k]=max(dp[i+4][j][k],xx+1);
                        dp[i+2][j+1][k]=max(dp[i+2][j+1][k],xx+1);
                        dp[i][j+2][k]=max(dp[i][j+2][k],xx+1);
                        dp[i][j+1][k+2]=max(dp[i][j+1][k+2],xx+1);
                        dp[i][j][k+4]=max(dp[i][j][k+4],xx+1);
                        dp[i+1][j][k+1]=max(dp[i+1][j][k+1],xx+1);
                        
                        if(i==u[1] && j==u[2] && k==u[3])
                        {
                            if(xx>tmp)
                            {
                                uu=1;
                                tmp=xx;
                            }
                        }
                        else
                        {
                            tmp=max(tmp,xx);
                        }
                    }
                }
            }
            //cout<<tmp<<endl;
            ans+=tmp;
        }
        
        if((u[1]==0 && u[2]==0 && u[3]==0) || uu==1)
        {
            ans--;
        }
        
        
        cout<<"Case #"<<times<<": "<<ans<<endl;
    }
    
    
    
    
    return 0;
} 
