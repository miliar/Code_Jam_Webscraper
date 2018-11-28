#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

char s[111];
char ans[111];
int n;
int t;
int main()
{
    int i,j,times;
    freopen("B-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    
    cin>>t;
    for(times=1;times<=t;times++)
    {
        cin>>s+1;
        n=strlen(s+1);
        
        for(i=n;i>=0;i--)
        {
            int la=-1;
            for(j=1;j<=i;j++)
            {
                if(la>s[j])break;
                la=s[j];
                ans[j]=s[j];
            }
            
            if(j<=i)
            {
                continue;
            }
            
            
            if(i+1<=n)
            {
                if(s[i+1]-1>=la)
                {
                    ans[i+1]=s[i+1]-1;
                    for(j=i+2;j<=n;j++)
                    {
                        ans[j]='9';
                    }
                    break;
                }
            }
            else
            {
                break;
            }
            
        }
        
        cout<<"Case #"<<times<<": ";
        bool st=0;
        for(i=1;i<=n;i++)
        {
            if(st==1 || ans[i]!='0')
            {
                cout<<ans[i];
                st=1;
            }
        }
        if(st==0)
        {
            cout<<0;
        }
        cout<<endl;
        
    }
    
    
    return 0;
} 
