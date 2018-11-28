#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define PR(x,a,b) {cout << #x << " = "; FOR(_,a,b) cout << x[_] << ' '; cout << endl;}
#define PB push_back
#define MP make_pair
#define BIT(s,i) (((s)&(1<<(i)))>0)
#define TWO(x) (1<<(x))
#define FI first
#define SE second
#define SZ(x) ((int)x.size())

const int MOD = 1000000007;
const double E = 1e-8;
const double PI = acos(-1);
const int NMAX = 2000;

priority_queue<ll, vector<ll>, greater<ll> > H;

int n, k;
ll r[NMAX];
ll h[NMAX];

pair<ll, ll> s[NMAX];

int main() {
  int stest;
  cin >> stest;
  FOR (test, 1, stest) {
    cout << "Case #" << test << ": ";
    cin >> n >> k;
    //BUG(n);
    FOR (i, 1, n) cin >> r[i] >> h[i];

    FOR (i, 1, n) s[i] = MP(r[i], (ll) 2 * r[i] * h[i]);

    sort(s + 1, s + n + 1);

    while (!H.empty()) H.pop();

    ll res = 0;
    ll ans = 0;

    FOR (i, 1, n) {
      if (i >= k) {
        res = max(res, s[i].FI * s[i].FI + s[i].SE + ans);
      }

      H.push(s[i].SE);
      ans += s[i].SE;

      if (i >= k) {
        ll x = H.top(); H.pop();
        ans -= x;
      }
    }

    printf("%.10lf\n", res * PI);
  }


}
