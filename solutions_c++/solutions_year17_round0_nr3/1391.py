#include <cstdio>
#include <map>
using namespace std;
#define fst first
#define snd second
typedef long long ll;
int t;
ll n,k;
map<ll,ll> mp;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas) {
        mp.clear();
        scanf("%I64d%I64d",&n,&k);
        printf("Case #%d: ",cas);
        if (k==1) {
            printf("%I64d %I64d\n",n/2,(n-1)/2);
            continue;
        }
        --k;
        ++mp[n/2];
        ++mp[(n-1)/2];
        while (mp.rbegin()->snd<k) {
            ll val=mp.rbegin()->fst,cnt=mp.rbegin()->snd;
            mp.erase(val);
            k-=cnt;
            if (val>=2)
                mp[val/2]+=cnt;
            if (val>=3)
                mp[(val-1)/2]+=cnt;
        }
        printf("%I64d %I64d\n",mp.rbegin()->fst/2,(mp.rbegin()->fst-1)/2);
    }
    return 0;
}
