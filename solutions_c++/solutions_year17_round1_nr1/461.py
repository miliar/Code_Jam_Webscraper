#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int n,m;
string a[26];

bool isgood(int r1, int r2, int c1, int c2, char c) {
  for (int i = r1; i <= r2; i++)
    for (int j = c1; j <= c2; j++) {
      if (a[i][j] != c && a[i][j] != '?') return false;
    }
  return true;
}

void go(int x, int y) {
  int li = x, ri = x, lj = y, rj = y;
  while (li > 0) {
    if (isgood(li-1,ri,lj,rj,a[x][y])) li--; else break;
  }
  while (lj > 0) {
    if (isgood(li,ri,lj-1,rj,a[x][y])) lj--; else break;
  }
  while (ri < n - 1) {
    if (isgood(li,ri+1,lj,rj,a[x][y])) ri++; else break;
  }
  while (rj < m - 1) {
    if (isgood(li,ri,lj,rj+1,a[x][y])) rj++; else break;
  }
  for (int i = li; i <= ri; i++)
    for (int j = lj; j <= rj; j++) {
      a[i][j] = a[x][y];
    }
}

void solve(int tc) {
  cout << "Case #" << tc << ": " << endl;
  cin >> n >> m;
  FOR(i, n) cin >> a[i];

  FOR(j, m) FOR (i, n)
  if (a[i][j] != '?') {
    go(i, j);
  }

  FOR(i,n) {
    FOR(j, m) cout << a[i][j];
    cout << endl;
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  int tt;
  cin >> tt;
  FOR(i, tt) {
    solve(i+1);
  }
  return 0;
}


