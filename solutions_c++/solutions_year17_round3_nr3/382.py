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
const ld eps = 1e-12;
const ld N = 10000;
const ll LOGN = 19;
const ld PI = 3.14159265358979323846;
ll mul(ll a, ll b, ll m = mod) { return (ll)(a * b) % m;}
ll add(ll a, ll b, ll m = mod) { a += b; if(a >= m) a -= m; if(a < 0) a += m; return a;}
ll power(ll a, ll b, ll m = mod) { if(b == 0) return 1; if(b == 1) return (a % m); ll x = power(a, b / 2, m); x = mul(x, x, m); if(b % 2) x = mul(x, a, m); return x;}
ll T, n, k;
ld p[55], u;
void test(ll tt)
{
    cin >> n >> k;
    cin >> u;
    map < ld , set < ll > > m;
    set < ld > s;
    f(i, n)
    {
        cin >> p[i];
        m[p[i]].insert(i);
        s.insert(p[i]);
    }
    ld rem = u;
    while(rem >= 0)
    {
        ld mi = *s.begin();
        s.erase(s.begin());
        if(s.size() == 0)
        {
            ld tot = (ld)m[mi].size();
            ld each = rem / tot;
            for(ll ids : m[mi])
            {
                p[ids] += each;
            }
            break;
        }
        ld mi2 = *s.begin();
        ld g = mi2 - mi;
        ld tot = (ld)m[mi].size();

        if(g * tot <= rem)
        {
            for(ll ids : m[mi])
            {
                p[ids] = mi2;
            }
            rem -= g  * tot;
        }
        else
        {
            ld each = rem / tot;
            for(ll ids : m[mi])
            {
                p[ids] += each;
            }
            break;
        }
        vector < ll > v;
        for(ll ids : m[mi])
        {
            v.pb(ids);
        }
        m[mi].clear();
        for(ll x : v)
        {
            s.insert(p[x]);
            m[p[x]].insert(x);
        }
    }
    ld ans = 1.0;
    f(i, n) ans = ans * p[i];

    cout << "Case #" << tt << ": ";
    cout << ans << "\n";
}
int main()
{
    ios_base::sync_with_stdio(0);
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("GCJ_Cs.out", "w", stdout);
    cin >> T;
    cout << fixed << setprecision(6);
    rep(i, 1, T) test(i);
    return 0;
}
