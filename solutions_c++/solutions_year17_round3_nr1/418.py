#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define eps 1e-9
#define MAX 100000
#define MAXL 20
#define MAXE 100000
#define inf 10000000000000000LL
#define pi acos(-1.0)
//ll mod = 1000000000+7;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
int n, k;
ll dp[1005][1005];
pll cake[1005];
bool cmp(pll a, pll b)
{
    if(a.ff == b.ff) return a.ss > b.ss;
    return a.ff > b.ff;
}
bool vis[1005][1005];
ll call(int pos, int taken) {
    if(taken == k) return 0;
    if(pos == n) return -inf;
    if(vis[pos][taken]) return dp[pos][taken];
    ll ret = -inf;
    if(taken == 0) ret = call(pos+1, taken+1)+cake[pos].ff*cake[pos].ff+2LL*cake[pos].ff*cake[pos].ss;
    else ret = call(pos+1, taken+1)+2LL*cake[pos].ff*cake[pos].ss;
    ret = max(ret, call(pos+1, taken));
    //D(ret);
    vis[pos][taken] = true;
    return dp[pos][taken] = ret;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    //ios_base::sync_with_stdio(false);

    int ncase, tcase = 1, i;
    scanf("%d", &ncase);
    while(ncase--) {
        scanf("%d %d", &n, &k);
        for(i = 0; i < n; i++) scanf("%lld %lld", &cake[i].ff, &cake[i].ss);
        mem(vis);
        sort(cake, cake+n, cmp);
        ll ans = call(0, 0);
       // D(ans);
        printf("Case #%d: %0.10lf\n", tcase++, ans*pi);
    }
    return 0;
}


