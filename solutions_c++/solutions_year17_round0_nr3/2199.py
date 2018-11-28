#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define f first
#define s second
#define in(x) scanf("%d",&x)
#define IN(x) scanf("%lld",&x)
#define inch(x) scanf("%s",x)
#define indo(x) scanf("%lf",&x)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int t;
ll n, k;
map<ll, ll>cnt;
set<ll>st;
set<ll>::iterator it;
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        IN(n); IN(k);
        printf("Case #%d: ",cases);
        st.clear();
        cnt.clear();
        st.insert(n);
        cnt[n] = 1LL;
        ll cur;
        while(k > 0){
            it = (--st.end());
            cur = (*it);
            k -= cnt[cur];
            st.erase(it);
            ll ffirst = cur / 2LL;
            ll ssecond = (cur - 1LL) / 2LL;
            cnt[ffirst] += cnt[cur];
            cnt[ssecond] += cnt[cur];
            st.insert(ffirst);
            st.insert(ssecond);
        }
        printf("%lld %lld\n",cur / 2LL, (cur - 1LL) / 2LL);
    }
    return 0;
}
