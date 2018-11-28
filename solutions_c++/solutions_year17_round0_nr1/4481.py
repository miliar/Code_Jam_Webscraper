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

int n, k, stest;
string s;

void flip(char &c) {
  if (c == '-') c = '+';
  else c = '-';
}

int main() {
  cin >> stest;
  FOR (test, 1, stest) {
    int res = 0;
    cout << "Case #" << test << ": ";
    cin >> s >> k;
    n = SZ(s);
    REP (i, n) if (i + k - 1 < n && s[i] == '-') {
      res ++;
      FOR (j, i, i + k - 1) flip(s[j]);
    }

    REP (i, n) if (s[i] == '-') res = -1;
    if (res == -1)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << res << endl;
  }
}
