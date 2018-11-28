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
ll n, m;
char a[26][26];
ll get(ll x, ll y, ll r, ll c) {
    ll ret = 0;
    for (ll i = x; i < r; i++) {
        for (ll j = y; j < c; j++) {
            if (a[i][j] != '?') {
                ret++;
            }
        }
    }
    return ret;
}

void solve(ll x, ll y, ll r, ll c) {
    if (get(x, y, r, c) == 1) {
        char w;
        for (ll i = x; i < r; i++) {
            for (ll j = y; j < c; j++) {
                if (a[i][j] != '?') {
                    w = a[i][j];
                    break;
                }
            }
        }
        for (ll i = x; i < r; i++) {
            for (ll j = y; j < c; j++) {
                a[i][j] = w;
            }
        }
    }
    for (ll i = x + 1; i < r; i++) {
        if (get(x, y, i, c) && get(i, y, r, c)) {
            solve(x, y, i, c);
            solve(i, y, r, c);
            return;
        }
    }

    for (ll i = y + 1; i < c; i++) {
        if (get(x, y, r, i) && get(x, i, r, c)) {
            solve(x, y, r, i);
            solve(x, i, r, c);
            return;
        }
    }
}

void solve(ll T)
{
    cin >> n >> m;
    f(i, n) f(j, m) cin >> a[i][j];
    solve(0, 0, n, m);
    cout << "Case #" << T << ":\n";
    f(i, n)
    {
        f(j, m) cout << a[i][j];
        cout << "\n";
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("a1l.out", "w", stdout);
    ll T;
    cin >> T;
    rep(i, 1, T) solve(i);
    return 0;
}
