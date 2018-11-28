#include <bits/stdc++.h>
using namespace std;
#define all(a)                        a.begin(), a.end()
#define minimum(a)                    *min_element(a.begin(), a.end())
#define maximum(a)                    *max_element(a.begin(), a.end())
#define cerr1(a)                    cerr << "[ " << a << " ]\n"
#define cerr2(a,b)                    cerr << "[ " << a << " , " << b << " ]\n"
#define cerr3(a,b,c)                cerr << "[ " << a << " , " << b << " , " << c << " ]\n"
#define fi                             first
#define se                             second
/*DAM SEHGAL*/
typedef long long ll;typedef long double ld;typedef vector<int> vi;typedef vector<char> vc;
typedef vector<string> vs;typedef vector<ll> vl;typedef set<int> si;typedef set<string> ss;
typedef map<int, int> mii;typedef map<string, int> msi;typedef pair<int, int> pii;
typedef pair<ll, ll> pll;typedef vector<pii> vii;typedef vector<vi> vvi;typedef vector<vii> vvii;
const int INF = 0x3f3f3f3f, MOD = 1e9 + 7;
ll power(ll a, ll n) {ll p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll power(ll a, ll n, ll mod) {ll p = 1;while (n > 0) {if(n%2) {p = p * a; p %= mod;} n >>= 1; a *= a; a %= mod;} return p % mod;}
ll add(ll a , ll b , ll mod = MOD){return (a + b) % mod;}
ll sub(ll a , ll b , ll mod = MOD){return ((a-b)%mod + mod)%mod;}
ll mul(ll a , ll b , ll mod = MOD){return (a * b) % mod;}
ll divide(ll a , ll b , ll mod = MOD){return (a * power(b,mod-2,mod))%mod;}
ll sqrt_floor(ll x){ll y = sqrt(x); while (y * y > x)--y; while ((y + 1) * (y + 1) <= x) ++y; return y;}
const ld pi = 3.14159265358888;
int n, k;
ll r[11], h[11];
ld ans = 0;


void Msort() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (r[i] < r[j]) {
                swap(r[i], r[j]);
                swap(h[i], h[j]);
            }
        }
    }
}

void area(int done, int i, int p, long long int sur) {
    if (done == k) {
        if (sur > ans)
            ans = sur;

        return;
    }


    if (i >= n)
        return;

    for (int j = i; j < n; j++) {
        long long int o = (2 * r[j] * h[j]) + (r[j] * r[j] - r[p] * r[p]);
        area(done + 1, j + 1, j, sur + o);
    }
}

int main(int argc, char const *argv[]) {

    int t;
    cin >> t;
    for (int l = 1; l <= t; l++) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> r[i] >> h[i];
        }
        Msort();
        for (int i = 0; i < n; i++) {
            long long int aa = (2 * r[i] * h[i] + r[i] * r[i]);

            area(1, i + 1, i, aa);
        }
        ans = ans * pi;
        cout << "Case #" << l << ": ";
        cout << fixed << setprecision(10) << ans << endl;
        ans = 0;


    }
}