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

int stest;

void calc(ll p1, ll p2, ll n, ll k) {
  if (p2 >= k) {
    cout << (n + 1) / 2 << " " << n / 2 << endl;
    return;
  }

  if (p1 + p2 >= k) {
    cout << n / 2 << " " << (n - 1) / 2 << endl;
    return;
  }

  if (n % 2 == 0)
    calc(p1, p1 + 2 * p2, (n - 1) / 2, k - p1 - p2);
  else
    calc(2 * p1 + p2, p2, (n - 1) / 2, k - p1 - p2);
}

int main() {
  cin >> stest;
  FOR (test, 1, stest) {
    ll n, k;
    cin >> n >> k;
    cout << "Case #" << test << ": ";
    calc(1, 0, n, k);
  }
}
