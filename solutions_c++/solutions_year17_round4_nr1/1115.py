#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define FORN(i, a, b) for (int i = (a); i < (b); i++)
#define REP(i, n) for (int i = 0; i < (n); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define BUG(x) cerr << #x << " = " << x << endl
#define PB push_back
#define MP make_pair

#define MAX 111

int n, p;
int a[MAX];
int f[MAX][MAX][MAX][5];

int nextL(int l, int s) {
  return ((l - s) + p) % p;
}

void op(int &f, int x) {
  if (f == -1 || f > x) f = x;
}

int main() {
  int ntest;
  cin >> ntest;
  FOR (test, 1, ntest) {
    cin >> n >> p;
    FOR (i, 1, n) cin >> a[i];
    FOR (i, 1, n) a[i] = a[i] % p;
    int c[5];

    memset(c, 0, sizeof(c));
    FOR (i, 1, n) if (a[i]) c[a[i]]++;

    memset(f, -1, sizeof(f));
    f[c[1]][c[2]][c[3]][0] = 0;

    int res = 1e9;
    FORD (i, c[1], 0) FORD (j, c[2], 0) FORD (k, c[3], 0) {
      FORD (l, p - 1, 0) {
        int &cur = f[i][j][k][l];
        if (cur == -1) continue;
        if (i == 0 && j == 0 && k == 0) res = min(res, cur);
        int d = l == 0 ? 0 : 1;
        if (i) {
          op(f[i - 1][j][k][nextL(l, 1)], cur + d);
        }
        if (j) {
          op(f[i][j - 1][k][nextL(l, 2)], cur + d);
        }
        if (k) {
          op(f[i][j][k - 1][nextL(l, 3)], cur + d);
        }
      }
    }
    cout << "Case #" << test << ": " << n - res << endl;
  }
}

