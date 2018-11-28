#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
string flip(string s,int n,int k)
{
    for(int i=n;i<n+k;i++)
    {
        if(s[i]=='-')
            s[i]='+';
        else
            s[i]='-';
    }
    return s;
}
int check(string s)
{
    for(int i=0;i<s.length();i++)
    {
        if(s[i]!='+')
            return 0;
    }
    return 1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("CJ17_1.out","w",stdout);
    int t,c;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        string s;
        int k,cnt=0;
        cin>>s>>k;
        int l=s.length();
        for(int i=0;i<l;i++)
        {
            if(i+k<=l)
            {
                if(s[i]=='-')
                {
                    s=flip(s,i,k);
                    cnt++;
                }
            }
        }
        cout<<"Case #"<<c<<": ";
        if(check(s)==0)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<cnt<<endl;
    }
}
