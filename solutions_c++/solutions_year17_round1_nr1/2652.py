#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>
using namespace std;

#define ll long long

int m,n;
string s[100];


int main() 
{
    freopen("input2.in","r",stdin);
    freopen("output.txt","w",stdout);
   
   int t;
   
   cin>>t;
   
   
   for(int k=1;k<=t;k++)
   {
        //cout<<"HI";
        char ch;
        cin>>m>>n;
        
        for(int i=0;i<=n+1;i++)
        {
            s[0][i]=s[m+1][i]='?';
        }
        
        for(int i=1;i<=m;i++)
        {
        cin>>s[i];
        s[i]='?'+s[i]+'?';
        }
        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(s[i][j]!='?')
                {
                    for(int l=j+1;l<=n;l++)
                    {
                        if(s[i][l]!='?')
                        break;
                        if(s[i][l]=='?')
                        s[i][l]=s[i][j];
                    }
                    for(int l=j-1;l>0;l--)
                    {
                        if(s[i][l]!='?')
                        break;
                        if(s[i][l]=='?')
                        s[i][l]=s[i][j];
                    }
                }
            }
        }
        for(int o=0;o<=55;o++)
        for(int i=1;i<=m;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if(s[i][j]=='?')
                {
                   if(s[i+1][j]!='?')
                   s[i][j]=s[i+1][j];
                   else
                   s[i][j]=s[i-1][j];
                }
            }
        }
        cout<<"Case #"<<k<<": "<<endl;
        for(int i=1;i<=m;i++)
        {
        for(int j=1;j<=n;j++)
        cout<<s[i][j];
        cout<<endl;
        }
   }
   
   
    return 0;
}
