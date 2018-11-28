#include<iostream>
#include<cmath>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int t,n,m;
char g[111][111];

int main()
{
    int i,j,k,times;
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    cin>>t;
    
    for(times=1;times<=t;times++)
    {
        cin>>n>>m;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                 cin>>g[i][j];
            }
        }
        
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(g[i][j]!='?')
                {
                    char u=g[i][j];
                    for(k=i-1;k>=1;k--)
                    {
                        if(g[k][j]=='?')
                        {
                            g[k][j]=u;
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
        
        for(j=1;j<=m;j++)
        {
            if(g[n][j]=='?')
            {
                k=n-1;
                while(k>0 && g[k][j]=='?')k--;
                
                if(k!=0)
                {
                    for(i=k+1;i<=n;i++)
                    {
                        g[i][j]=g[k][j];
                    }
                }
            }
        }
        ////////////////////////////////////////////////////
        
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                if(g[i][j]!='?')
                {
                    char u=g[i][j];
                    for(k=j-1;k>=1;k--)
                    {
                        if(g[i][k]=='?')
                        {
                            g[i][k]=u;
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
        }
        
        for(i=1;i<=n;i++)
        {
            if(g[i][m]=='?')
            {
                k=m-1;
                while(k>0 && g[i][k]=='?')k--;
                
                if(k!=0)
                {
                    for(j=k+1;j<=m;j++)
                    {
                        g[i][j]=g[i][k];
                    }
                }
            }
        }
        
        cout<<"Case #"<<times<<":"<<endl;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cout<<g[i][j];
            }
            cout<<endl;
        }
    }
    
    
    
    return 0;
}
