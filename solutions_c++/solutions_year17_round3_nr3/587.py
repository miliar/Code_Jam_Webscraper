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
const double E = 1e-4;
const double PI = acos(-1);
const int NMAX = 1000;

int n, m, k, stest;
int p[NMAX];
priority_queue<int, vector<int>, greater<int> > H;

int main() {
  cin >> stest;
  FOR (test, 1, stest) {
    cin >> n >> k;
    double tmp;
    cin >> tmp;
    m = (int) (tmp * 10000 + E);

    FOR (i, 1, n) {
      cin >> tmp;
      p[i] = (int) (tmp * 10000 + E);
    }

    FOR (i, 1, n) H.push(p[i]);
    while (m > 0) {
      m--;
      int x = H.top(); H.pop();
      H.push(x + 1);
    }

    double res = 1.0;
    while (!H.empty()) {
      int x = H.top(); H.pop();
      res *= x / 10000.0;
    }

    printf("Case #%d: %.7lf\n", test, res);
  }
}
