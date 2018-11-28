#include <iostream>
#include <string>
using namespace std;

int main()
{
    int tc,tci=0;
    cin>>tc;
    while(tc--)
    {
        tci++;
        string s;
        int k,ct=0;
        cin>>s>>k;
        int i,j;
        for(i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='+')continue;
            ct++;
            for(j=i;j<i+k;j++)
            {
                if(s[j]=='+')s[j]='-';
                else s[j]='+';
            }
        }
        int fl=0;
        for(;i<s.size();i++)if(s[i]=='-')
        {
            fl=1;
            break;
        }
        cout<<"Case #"<<tci<<": ";
        if(fl==1)cout<<"IMPOSSIBLE"<<endl;
        else cout<<ct<<endl;
    }
    return 0;
}
