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
const ld eps = 1e-3;
const ll N = 1000005;
const ll LOGN = 19;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m = mod) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m = mod) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m = mod) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll n, p, r[55], q[55][55];
pair < ll , ll > get(ld a, ld b)
{
    ll ma = (ll)(a * 10) / b;
    ll l = 1, r1 = ma, s = -1;
    while(l <= r1)
    {
        ll m = l + r1 >> 1;
        ld x1 = b * m * 0.9;
        ld x2 = b * m * 1.1;
        if(x1 - eps <= a && a <= x2 + eps)
        {
            s = m;
            r1 = m - 1;
        }
        else if(x1 - eps > a)
        {
            r1 = m - 1;
        }
        else
        {
            l = m + 1;
        }
    }
    l = 1, r1 = ma;
    ll e = -1;
    while(l <= r1)
    {
        ll m = l + r1 >> 1;
        ld x1 = b * m * 0.9;
        ld x2 = b * m * 1.1;
        if(x1 - eps <= a && a <= x2 + eps)
        {
            e = m;
            l = m + 1;
        }
        else if(x1 - eps > a)
        {
            r1 = m - 1;
        }
        else
        {
            l = m + 1;
        }
    }
    return {s, e};
}
pair < ll , ll > t[55][55];
bool FindMatch(ll i, const vector<vector<ll> > &w, vector<ll> &mr, vector<ll> &mc, vector<ll> &seen)
{
    for (ll j = 0; j < w[i].size(); j++)
    {
        if (w[i][j] && !seen[j])
        {
            seen[j] = true;
            if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen))
            {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}
ll BipartiteMatching(const vector<vector<ll> > &w, vector<ll> &mr, vector<ll> &mc)
{
    mr = vector<ll>(w.size(), -1);
    mc = vector<ll>(w[0].size(), -1);
    ll ct = 0;
    for (ll i = 0; i < w.size(); i++)
    {
        vector<ll> seen(w[0].size());
        if (FindMatch(i, w, mr, mc, seen)) ct++;
    }
    return ct;
}
void solve(ll T)
{
    cin >> n >> p;
    memset(q, 0, sizeof(q));
    memset(r, 0, sizeof(r));
    f(i, n) cin >> r[i];
    f(i, n) f(j, p) cin >> q[i][j];
    f(i, n)
    {
        f(j, p)
        {
            ld a = q[i][j] + 0.0;
            ld b = r[i] + 0.0;
            t[i][j] = get(a, b);
        }
    }
    ll ans = 0;
    if(n == 1)
    {
        ans = 0;
        f(i, p) if(t[0][i].F != -1) ans++;
    }
    else
    {
        vector < vector < ll > > can;
        can.resize(p, vector < ll > (p));
        f(i, p)
        {
            f(j, p)
            {
                ll e = t[0][i].S, s = t[0][i].F, s1 = t[1][j].F, e1 = t[1][j].S;
                if(s == -1 || s1 == -1) continue;
                assert(e != -1);
                assert(e1 != -1);
                if(s1 <= e && e <= e1)
                {
                    can[i][j] = 1;
                }
                else if(s <= e1 && e1 <= e)
                {
                    can[i][j] = 1;
                }
            }
        }
        vector < ll > tmp, tmp2;
        ans = BipartiteMatching(can, tmp, tmp2);
    }
    cout << "Case #" << T << ": ";
    cout << ans << "\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("b1s2.out", "w", stdout);
    ll T;
    cin >> T;
    rep(i, 1, T) solve(i);
    return 0;
}
