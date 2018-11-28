#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<map>
using namespace std;
typedef long long ll;
map<ll,ll>mp;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        ll n,k;
        scanf("%lld%lld",&n,&k);
        ll las=-1;
        mp.clear();
        mp[n]=1;
        while(k>0)
        {
            ll len=(--mp.end())->first;
            ll cnt=(--mp.end())->second;
            mp.erase(--mp.end());
            k-=cnt;
            mp[len/2]+=cnt;
            mp[(len-1)/2]+=cnt;
            las=len;
        }
        printf("Case #%d: %lld %lld\n",ca,las/2,(las-1)/2);
    }
    return 0;
}
