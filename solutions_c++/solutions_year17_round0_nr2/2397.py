#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;


ll t,n;

vector<ll> num;

void gen(ll d,int lv,int l,int len)
{
    if(l==len)
    {
        num.push_back(d);
        return;
    }

    for(ll i=lv; i<10; i++)
    {
        gen(d*10+i,i,l+1,len);
    }
}


int main()
{
    freopen("B-large.in","rt",stdin);
    freopen("out.txt","wt",stdout);

    for(int i=1; i<19; i++)
        gen(0,1,0,i);

    cin>>t;
    for(int c=1; c<=t; c++)
    {
        cin>>n;

        ll ans=1;
        for(int i=0; i<num.size(); i++)
            if(num[i]<=n)ans=num[i];

        cout<<"Case #"<<c<<": "<<ans<<endl;


    }

    return 0;
}
