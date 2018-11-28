#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    string s[n];
    int f[n],count=0,m[n],x;
    for(int i=0;i<n;i++)
    {
        cin>>s[i]>>f[i];
        m[i] = (s[i].size())/f[i];
    }
    for(int i=0;i<n;i++)
    {
        int j;
        count=0;
        for(j=0;j <= (s[i].size() - f[i]);j++)
       {
            if(s[i][j]=='-')
          {
              count++;
                for(int k=j;k<j+f[i];k++)
            {
                if(s[i][k]=='-') s[i][k]='+';
                else s[i][k]='-';
            }
          }
        }
        x=1;
        for(;j<s[i].size();j++)
        {
            if(s[i][j]=='-')
                {
                    x=0;
                }
        }
        if(x==0)
            cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<count<<endl;
    }
}
