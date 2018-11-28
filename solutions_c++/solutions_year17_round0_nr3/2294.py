#include<bits/stdc++.h>
#define ll long long,long long
#define mk make_pair
using namespace std;
typedef pair<ll> PLL;
map<ll>s;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out31.out","w",stdout);
    int Q;
    long long n,k,now;
    cin >> Q;
    for(int i=1;i<=Q;i++)
    {
        cin >> n >> k;
        s.clear();
        s.insert(mk(n,1));
        while(2)
        {
            map <ll>::iterator ite = s.end();
            ite--;
            k-=(*ite).second;
            now = (*ite).first;
            now--;
            if(k<=0)
            {
                printf("Case #%d: %lld %lld\n",i,max(now/2,now-(now/2)),min(now/2,now-(now/2)));
                goto u;
            }
            s.erase(ite);
            s[now/2]+=(*ite).second;
            s[now - now/2]+=(*ite).second;
        }
        u:;
    }
    return 0;
}
