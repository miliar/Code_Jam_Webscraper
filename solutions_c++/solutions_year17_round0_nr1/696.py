#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

int t,k;
char s[2011];
int ans;
int n;
int main()
{
    int i,j,times;
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    
    cin>>t;
    for(times=1;times<=t;times++)
    {
        cin>>s+1>>k;
        ans=0;
        n=strlen(s+1);
        
        //cout<<n<<"!!!!"<<endl;
        for(i=1;i<=n-k+1;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(j=i;j<=i+k-1;j++)
                {
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                }
            }
        }
        
        for(i=n-k+2;i<=n;i++)
        {
            if(s[i]=='-')
            {
                ans=-1;
            }
        }
        
        
        if(ans==-1)
        {
            cout<<"Case #"<<times<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        
        cout<<"Case #"<<times<<": "<<ans<<endl;
        
    }
    
    
    return 0;
} 
