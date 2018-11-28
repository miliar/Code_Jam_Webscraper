#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll,ll> mp;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        mp.clear();
        ll n,k,len,num;
        scanf("%lld%lld",&n,&k);
        mp[n]=1;
        while(k>0)
        {
            auto it=mp.end();
            --it;
            len=it->first;
            num=it->second;
            mp.erase(it);
            k-=num;
            if(mp.count(len/2)) mp[len/2]+=num;
            else mp[len/2]=num;
            if(mp.count((len-1)/2)) mp[(len-1)/2]+=num;
            else mp[(len-1)/2]=num;
        }
        printf("Case #%d: %lld %lld\n",cas,len/2,(len-1)/2);
    }
}
