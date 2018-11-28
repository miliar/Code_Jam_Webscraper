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
const int NMAX = 1444;

int n, m, stest;
int fre[2][NMAX];
int dp[NMAX][NMAX][2];

int main() {
  cin >> stest;
  FOR (test, 1, stest) {
    cin >> n >> m;
    FOR (i, 1, 1440) fre[0][i] = fre[1][i] = true;
    FOR (i, 1, n) {
      int u, v; cin >> u >> v;
      FOR (t, u + 1, v) fre[0][t] = false;
    }
    FOR (i, 1, m) {
      int u, v; cin >> u >> v;
      FOR (t, u + 1, v) fre[1][t] = false;
    }

    int res = MOD;

    FOR (start, 0, 1) {
      FOR (i, 0, 1440) FOR (j, 0, 720) FOR (t, 0, 1) dp[i][j][t] = MOD;
      dp[0][0][start] = 0;
      FOR (i, 0, 1440 - 1) FOR (j, 0, 720) FOR (t, 0, 1) if (dp[i][j][t] < MOD) {
        if (fre[0][i+1] && j < 720)
          dp[i+1][j+1][0] = min(dp[i+1][j+1][0], dp[i][j][t] + (t == 1));
        if (fre[1][i+1] && i - j < 720) {
          dp[i+1][j][1] = min(dp[i+1][j][1], dp[i][j][t] + (t == 0));
        }
      }

      res = min(res, dp[1440][720][start]);
    }

    cout << "Case #" << test << ": " << res << endl;
  }
}
