#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;
ll n;
map<ll,ll> res;
ll solve (ll curr_max,ll pos,ll curr_num){
res[curr_num]++;
if(curr_num>n)
return 0;


ll res=curr_num;
for(ll i=1;i<=curr_max;i++){
ll tmp=i*pow(10,pos);
res=max(res,solve(i,pos+1,curr_num+tmp));
}

return res;
}
int main()
{
    n=1000000000000000000;
    ll x=solve(9,0,0);
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    ll t;
    cin>>t;
    for(ll i=0;i<t;i++){
        cin>>n;
        ll ans=1;
        for(auto it=res.begin();it!=res.end();it++)
        {
            if(it->first>n)
            break;
            ans=it->first;
        }
    cout<<"Case #"<<i+1<<": "<<ans<<endl;


    }
    return 0;
}
