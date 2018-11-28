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
#define sz(x) ((int)x.size())
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
const ll inf = (ll)5e16;
const ld eps = 1e-12;
const ll N = 205;
const ll LOGN = 19;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll n, p, g[N];
void test(ll tt)
{
    cin >> n >> p;
    f(i, n) cin >> g[i];
    ll ans = 0;
    if(p == 2)
    {
        ll c1 = 0;
        f(i, n) if(g[i] % p == 1) c1++;
        ans = c1 / 2;
    }
    else if(p == 3)
    {
        ll c[3] = {};
        f(i, n) c[g[i] % p]++;
        if(c[1] < c[2])
        {
            ans = c[1] + 2 * ((c[2] - c[1]) / 3) + max(0ll, (c[2] - c[1]) % 3 - 1);
        }
        else if(c[2] < c[1])
        {
            ans = c[2] + 2 * ((c[1] - c[2]) / 3) + max(0ll, (c[1] - c[2]) % 3 - 1);
        }
        else
        {
            ans = c[1];
        }
    }
    ans = n - ans;
    cout << "Case #" << tt << ": ";
    cout << ans << "\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("G2As1.out", "w", stdout);
    ll T;
    cin >> T;
    rep(i, 1, T) test(i);
    return 0;
}
