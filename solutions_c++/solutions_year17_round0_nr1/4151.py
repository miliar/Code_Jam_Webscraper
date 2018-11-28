#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        string s;
        cin>>s;
        int n,count=0;
        cin>>n;
        for(int i=0;i<s.length()-n+1;i++)
        {
            if(s[i]=='-')
            {
                for(int k=i;k<i+n;k++)
                {
                    if(s[k]=='-')    s[k]='+';
                    else    s[k]='-';
                }
                count++;
            }
        }
        bool flag=false;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
                flag=true;
        }
        cout<<"Case #"<<j<<": ";
        if(flag)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<count<<endl;
    }
   return 0;
}