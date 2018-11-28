// @formatter:off
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vector<int> > vvi;
typedef vector<ll> vl;
typedef vector<vector<ll> > vvl;
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define X first
#define Y second
template<class T> inline T sqr(T x) { return x * x; }
template<class T> inline T parse(const string&s){T x;stringstream ss(s);ss>>x;return x;}
int gcd(int a,int b){return a?gcd(b%a,a):b;}
ll gcd(ll a,ll b){return a?gcd(b%a,a):b;}
ll powmod(ll a,ll p,ll m){ll r=1;while(p){if(p&1)r=r*a%m;p>>=1;a=a*a%m;}return r;}
// @formatter:on


void solveTest() {
    int n, p;
    cin >> n >> p;
    vi a(n);
    forn(i, n) cin >> a[i];
    forn(i, n) a[i] %= p;
    int v0 = 0;
    int v1 = 0;
    int v2 = 0;
    int res = 0;
    forn(i, n) if (a[i] == 0) v0++;
    forn(i, n) if (a[i] == 1) v1++;
    forn(i, n) if (a[i] == 2) v2++;
    res += v0;
    if (p == 2) res += (v1 + 1) / 2;
    if (p == 3) {
        int k = min(v1, v2);
        v1 -= k;
        v2 -= k;
        res += k;
        k = max(v1, v2);
        res += (k + 2) / 3;
    }

    cout << res;

}

int main() {
#ifdef EFGEN_DBG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        solveTest();
        cout << endl;
    }
}
