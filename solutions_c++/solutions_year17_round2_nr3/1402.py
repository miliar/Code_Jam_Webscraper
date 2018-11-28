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
const ll inf = (ll)5e10;
const ld eps = 1e-7;
const ll N = 1005;
const ll LOGN = 19;
const ld inf1 = 5e12;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m = mod) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m = mod) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m = mod) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll n, q, e[N], s[N], d[N], sum[N];
ld dp[N][N];
bool done[N][N];
ld solve(ll i, ll h)
{
    if(i == n - 1) return 0.0;
    if(done[i][h]) return dp[i][h];
    ld ans = inf1;
    done[i][h] = 1;
    ld t = (d[i] + 0.0) / (s[h] + 0.0);
    ld t2 = (d[i] + 0.0) / (s[i] + 0.0);
    if(sum[i] - (h ? sum[h - 1] : 0) <= e[h]) ans = min(ans, t + solve(i + 1, h));
    if(d[i] <= e[i]) ans = min(ans, t2 + solve(i + 1, i));
    return dp[i][h] = ans;
}
void solve1(ll tt)
{
    cin >> n >> q;
    f(i, n) cin >> e[i] >> s[i];
    memset(done, false, sizeof(done));
    f(i, n) f(j, n)
    {
        ll x;
        cin >> x;
        if(j == i + 1) d[i] = x;
    }
    f(i, n - 1)
    {
        sum[i] = (i ? sum[i - 1] : 0) + d[i];
    }
    f(i, q)
    {
        ll u, v;
        cin >> u >> v;
    }
    ld ans = solve(0, 0);
    cout << "Case #" << tt << ": " << ans << "\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("GCJ_Cs.out", "w", stdout);
    cout << fixed << setprecision(7);
    ll T;
    cin >> T;
    rep(i, 1, T) solve1(i);
    return 0;
}
