#include <bits/stdc++.h>
using namespace std;

#define ms(s, n) memset(s, n, sizeof(s))
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORd(i, a, b) for (int i = (a) - 1; i >= (b); i--)
#define FORall(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define sz(a) int((a).size())
#define present(t, x) (t.find(x) != t.end())
#define all(a) (a).begin(), (a).end()
#define uni(a) (a).erase(unique(all(a)), (a).end())
#define pb push_back
#define pf push_front
#define mp make_pair
#define fi first
#define se second
#define prec(n) fixed<<setprecision(n)
#define bit(n, i) (((n) >> (i)) & 1)
#define bitcount(n) __builtin_popcountll(n)
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vii;
const int MOD = (int) 1e9 + 7;
const int INF = (int) 1e9;
const ll LINF = (ll) 1e18;
const ld PI = acos((ld) -1);
const ld EPS = 1e-9;
inline ll gcd(ll a, ll b) {ll r; while (b) {r = a % b; a = b; b = r;} return a;}
inline ll lcm(ll a, ll b) {return a / gcd(a, b) * b;}
inline ll fpow(ll n, ll k, int p = MOD) {ll r = 1; for (; k; k >>= 1) {if (k & 1) r = r * n % p; n = n * n % p;} return r;}
template<class T> inline int chkmin(T& a, const T& val) {return val < a ? a = val, 1 : 0;}
template<class T> inline int chkmax(T& a, const T& val) {return a < val ? a = val, 1 : 0;}
inline ll isqrt(ll k) {ll r = sqrt(k) + 1; while (r * r > k) r--; return r;}
inline ll icbrt(ll k) {ll r = cbrt(k) + 1; while (r * r * r > k) r--; return r;}
inline void addmod(int& a, int val, int p = MOD) {if ((a = (a + val)) >= p) a -= p;}
inline void submod(int& a, int val, int p = MOD) {if ((a = (a - val)) < 0) a += p;}
inline int mult(int a, int b, int p = MOD) {return (ll) a * b % p;}
inline int inv(int a, int p = MOD) {return fpow(a, p - 2, p);}
inline int sign(ld x) {return x < -EPS ? -1 : x > +EPS;}
inline int sign(ld x, ld y) {return sign(x - y);}
#define db(x) cerr << #x << " = " << (x) << ", ";
#define endln cerr << "\n";
#define chkpt cerr << "-----\n";

const int maxn = 100 + 5;
int n, p;
int a[maxn];
int dp[maxn][maxn][maxn];

int func(int r1, int r2, int r3) {
    int& res = dp[r1][r2][r3];
    if (~res) return res;
    res = 0;
    
    if (r1 + r2 + r3) {
        chkmax(res, 1);
    }
    
    if (r1 && r3) {
        chkmax(res, func(r1 - 1, r2, r3 - 1) + 1);
    }
    if (r1 >= 2 && r2 >= 1) {
        chkmax(res, func(r1 - 2, r2 - 1, r3) + 1);
    }
    if (r1 >= 4) {
        chkmax(res, func(r1 - 4, r2, r3) + 1);
    }
    if (r2 >= 2) {
        chkmax(res, func(r1, r2 - 2, r3) + 1);
    }
    if (r2 >= 1 && r3 >= 2) {
        chkmax(res, func(r1, r2 - 1, r3 - 2) + 1);
    }
    if (r3 >= 4) {
        chkmax(res, func(r1, r2, r3 - 4) + 1);
    }
    
    return res;
}

int solve4() {
    ms(dp, -1);
    cout << func(a[1], a[2], a[3]) + a[0] << "\n";
}

void solve() {
    int test; cin >> test;
    FOR(it, 1, test + 1) {
        cout << "Case #" << it << ": ";
        cin >> n >> p;
        ms(a, 0);
        FOR(i, 0, n) {
            int x; cin >> x; a[x % p]++;
        }
        if (p == 4) {
            solve4();
            continue;
        }
        int ans = a[0];
        for (int i = 1; i + i < p; i++) {
            while (a[i] && a[p - i]) {
                ans++;
                a[i]--, a[p - i]--;
            }
        }
        if (!(p & 1)) {
            while (a[p / 2] >= 2) {
                ans++;
                a[p / 2] -= 2;
            }
        }
        if (p == 2) {
            ans += a[1];
            cout << ans << "\n";
        }
        else if (p == 3) {
            while (a[1] >= 3) {
                ans++;
                a[1] -= 3;
            }
            while (a[2] >= 3) {
                ans++;
                a[2] -= 3;
            }
            ans += (a[1] + a[2] > 0);
            cout << ans << "\n";
        }
    }
}

int main() {
    int JUDGE_ONLINE = 1;
    if (fopen("in.txt", "r")) {
        JUDGE_ONLINE = 0;
        assert(freopen("in.txt", "r", stdin));
        assert(freopen("out.txt", "w", stdout));
    }
    else {
        ios_base::sync_with_stdio(0), cin.tie(0);
    }
    solve();
    if (!JUDGE_ONLINE) {
        //cout << "\nTime elapsed: " << 1000 * clock() / CLOCKS_PER_SEC << "ms\n";
    }
    return 0;
}
