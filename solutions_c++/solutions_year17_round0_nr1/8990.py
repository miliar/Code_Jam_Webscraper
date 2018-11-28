#include<bits/stdc++.h>
#include<iostream>
#include<string>
using namespace std;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    string s;
    int i,j,tt;
    cin>>tt;
    for(i=1; i<=tt; i++)
    {
        int moves = 0;
        int k;
        cin>>s>>k;
        int len=s.size()-k;
        for(int j = 0; j<=len; j++)
        {
            if(s[j]=='-')
            {
                moves++;
                for(int i=j; i<=j+k-1; i++)
                {
                  if(s[i]=='+')
                  {
                      s[i]='-';
                  }
                  else
                  {
                      s[i]='+';
                  }
                }
            }
        }
        int c=0;
        for(int i=0; i<s.size(); i++)
        {

           if(s[i]=='-')c=1;
        }
       if(c!=1)
       cout<<"Case #"<<i<<": "<<moves<<"\n";
       else
        cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";
    }
    return 0;
}
