#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    ll t;
    cin>>t;
    for(ll tt=1;tt<=t;tt++)
    {
        ll n,k;
        cin>>n>>k;
        priority_queue<pair<ll,pair<ll,ll> > > pq;
        pq.push({n,{1,n}});
        k--;
        while(k-->0 && !pq.empty())
        {
            ll tl,tr;
            tl=pq.top().second.first,tr=pq.top().second.second;
            pq.pop();
            ll fl,fs,sl,ss;
            fl=tl,fs=(tl+tr)/2-1,sl=(tl+tr)/2+1,ss=tr;
            if(fs-fl+1>1)
                pq.push({fs-fl+1,{fl,fs}});
            if(ss-sl+1>0)
                pq.push({ss-sl+1,{sl,ss}});
        }
        printf("Case #%lld: ",tt);
        if(pq.empty())
        {
            cout<<0<<" "<<0<<endl;
            continue;
        }
        ll len=pq.top().first;
        if(len%2)
            cout<<len/2<<" "<<len/2<<endl;
        else
            cout<<len/2<<" "<<len/2-1<<endl;
    }
    return 0;
}