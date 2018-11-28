#include<bits/stdc++.h>
#define ll unsigned long long
#define pb push_back
using namespace std;
int main()
{
    ll tc,n,j,k,flag,z;
    vector<ll>v;
    cin>>tc;
    for(ll q=1;q<=tc;++q)
    {
       cin>>n;
    v.clear();
    while(n)
    {
        j=n%10;
        v.pb(j);
        n/=10;
    }
    reverse(begin(v),end(v));
    flag=v.size();
    if(v.size()==1)
    cout<<"Case #"<<q<<": "<<v[0]<<"\n";
    else
    {
       for(j=v.size()-1;j>0;--j)
       {
           if(v[j-1]>v[j])
           {
               --v[j-1];
               flag=j;
           }
       }
        if(v[0]==0)
        {  cout<<"Case #"<<q<<": ";
            for(j=0;j<v.size()-1;++j)
            cout<<"9";
        }
        else{ cout<<"Case #"<<q<<": ";
       for(j=0;j<flag;++j)
       cout<<v[j];
       for(j=flag;j<v.size();++j)
       cout<<"9";
    }
    cout<<"\n";
    }
    }
    return 0;
}