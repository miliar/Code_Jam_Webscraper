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
const ll inf = (ll)5e16;
const ld eps = 1e-12;
const ll N = 1000005;
const ll LOGN = 19;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m = mod) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m = mod) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m = mod) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll t, ans[10006];
void solve(ll t)
{
    ll n;
    cin >> n;
    cout << "Case #" << t << ": " << ans[n] << "\n";
}
bool is(ll x)
{
    vector < ll > v;
    while(x)
    {
        v.pb(x % 10);
        x /= 10;
    }
    for(ll i = 0; i < v.size() - 1; i++)
    {
        if(v[i] < v[i + 1]) return false;
    }
    return true;
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("Bs1.out", "w", stdout);
    cin >> t;
    ll c = 1;
    for(ll i = 1; i <= 1000; i++)
    {
        if(is(i)) ans[i] = i;
        else ans[i] = ans[i - 1];
    }
    rep(i, 1, t) solve(i);
    return 0;
}
