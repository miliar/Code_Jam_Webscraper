#include <iostream>
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    ll t;
    cin>>t;
    for(int f=1;f<=t;f++)
    {
        string x;
        ll k;
        cin>>x>>k;
        ll ans=0;
        bool res=0;
        for(int i=0;i<x.size();i++)
        {
            if(x[i]=='+')continue;
            int temp=i;
            if(i+k>x.size())
            {
                res=1;
                break;
            }
            for(int j=0;j<k;j++,temp++)
            {
                if(x[temp]=='+')x[temp]='-';
                else x[temp]='+';
            }
            ans++;
        }
        cout<<"Case #"<<f<<": ";
        if(res)cout<<"IMPOSSIBLE";
        else cout<<ans;
        if(f<t)cout<<endl;
    }
    return 0;
}
