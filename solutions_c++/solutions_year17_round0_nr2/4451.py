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
const int NMAX = 1000;

int n, stest;
ll k;

int main() {
  cin >> stest;
  FOR (test, 1, stest) {
    cin >> k;
    ll tmp = k;
    n = 0;
    while (tmp > 0) { tmp /= 10; n++; }

    ll res = 0;
    int last = 0;
    FOR (i, 1, n) {
      FORD (cs, 9, last) {
        ll tmp = res;
        FOR (j, i, n) tmp = tmp * 10 + cs;
        if (tmp <= k) {
          res = res * 10 + cs;
          last = cs;
          break;
        }
      }
    }

    cout << "Case #" << test << ": " << res << endl;
  }
}
