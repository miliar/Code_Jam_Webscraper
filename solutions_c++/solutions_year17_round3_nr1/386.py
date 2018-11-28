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
const ld inf = 5e14;
const ld eps = 1e-12;
const ll N = 1005;
const ll LOGN = 19;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m = mod) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m = mod) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m = mod) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll T, n, k;
ld dp[N][N];
pair < ld , ld > a[N];
bool done[N][N];

ld solve(ll i, ll d)
{
    if(d == k)
    {
        return 0;
    }
    if(i == n) return -inf;
    if(done[i][d]) return dp[i][d];
    ld ret = 0;
    for(ll j = i + 1; j <= n; j++)
    {
        ld curr = 2.0 * PI * a[i].F * a[i].S + PI * a[i].F * a[i].F - PI * a[j].F * a[j].F + solve(j, d + 1);
        ret = max(ret, curr);
    }
    done[i][d] = 1;
    return dp[i][d] = ret;
}
void test(ll tt)
{
    cin >> n >> k;
    f(i, n) cin >> a[i].F >> a[i].S;
    a[n].F = a[n].S = 0;
    sort(a, a + n);
    reverse(a, a + n);
    ld ans = 0;
    f(i, n + 2) f(j, n + 2) done[i][j] = false;
    f(i, n + 2) f(j, n + 2) dp[i][j] = 0.0;
    for(ll i = 0; i < n; i++)
    {
        ans = max(ans, solve(i, 0));
    }

    cout << "Case #" << tt << ": ";
    cout << ans << "\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("GCJC_Al.out", "w", stdout);

    cout << fixed << setprecision(9);
    cin >> T;
    rep(i, 1, T) test(i);
    return 0;
}
