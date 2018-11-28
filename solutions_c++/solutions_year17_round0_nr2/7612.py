#include <iostream>
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
bool good(string x)
{
    for(int i=1;i<x.size();i++)
    {
       if(x[i]<x[i-1])return 0;
    }
    return 1;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    ll t;
    cin>>t;
    for(int f=1; f<=t; f++)
    {
        string x;
        cin>>x;
        int idx;
        while(!good(x))
        {
            for(int i=0; i<x.size()-1; i++)
            {
               if(x[i]>x[i+1])
               {
                   idx=i;
                   break;
               }
            }
            x[idx]=x[idx]-1;
            for(int i=idx+1;i<x.size();i++)x[i]='9';
        }
        cout<<"Case #"<<f<<": ";
        ll ch=0;
        for(int i=0;i<x.size();i++)
            if(ch)cout<<x[i];
        else
        {
            if(x[i]!='0')
            {
                ch=1;
                cout<<x[i];
            }
        }
        if(f<t)cout<<endl;
    }
    return 0;
}
