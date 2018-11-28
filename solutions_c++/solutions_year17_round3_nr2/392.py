#include<bits/stdc++.h>
using namespace std;
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pl;

#define sl(x) scanf("%lld",&x)
#define pl(x) printf("%lld\n",x)
#define sf(x) sort(x.begin(),x.end(),func)
#define s(x) sort(x.begin(),x.end())
#define all(v) v.begin(),v.end()
#define rs(v) { s(v) ; r(v) ; }
#define r(v) {reverse(all(v));}
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define f(i,n) for(int i=0;i<n;i++)
#define rep(i,a,b) for(int i=a;i<=b;i++)

const ll mod = 1000000007;
const ll inf = (ll)2000;
const ld eps = 1e-12;
const ll N = 1000005;
const ll LOGN = 19;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m = mod) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m = mod) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m = mod) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll T, ac, aj;
ll w[2][1444];
ll dp[2][1444][722];
ll in;
ll solve(ll t, ll c, ll d)
{
    if(t == 24 * 60)
    {
        if(d != 720)
        {
            return inf;
        }
        return (c != in);
    }
    if(d > 720) return inf;
    if(dp[c][t][d] != -1) return dp[c][t][d];
    ll ret = inf;
    if(!w[c][t + 1])
    {
        ret = min(ret, solve(t + 1, c, d + (c == 0)));
    }
    if(!w[1 - c][t + 1])
    {
        ret = min(ret, 1 + solve(t + 1, 1 - c, d + (c == 0)));
    }
    return dp[c][t][d] = ret;
}
void test(ll tt)
{
    cin >> ac >> aj;
    f(i, 2) f(j, 1444) w[i][j] = 0;
    f(i, ac)
    {
        ll c, d;
        cin >> c >> d;
        rep(j, c, d - 1) w[0][j] = 1;
    }
    f(i, aj)
    {
        ll c, d;
        cin >> c >> d;
        rep(j, c, d - 1) w[1][j] = 1;
    }
    memset(dp, -1, sizeof(dp));
    ll ans = inf;
    if(!w[0][0])
    {
        in = 0;
        ans = min(ans, solve(0, 0, 0));
    }
    if(!w[1][0])
    {
        in = 1;
        memset(dp, -1, sizeof(dp));
        ans = min(ans, solve(0, 1, 0));
    }
    cout << "Case #" << tt << ": ";
    cout << ans;
    cout << "\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("GCJ_Bl.out", "w", stdout);
    cin >> T;
    rep(i, 1, T) test(i);
    return 0;
}
