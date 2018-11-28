#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <assert.h>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)
#define INF 2000000000


using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int r, c;
char a[5][50];
bool ban[5][50][3];

// 1 |, 2 -

bool check(int x, int y) {
  for (int i = x+1; i < r; i++) {
    if (a[i][y] == '-' || a[i][y] == '|') {
      ban[x][y][1] = 1;
      a[x][y] = '-';
      break;
    } else if (a[i][y] == '#') break;
  }

  for (int i = x-1; i >= 0; i--) {
    if (a[i][y] == '-' || a[i][y] == '|') {
      ban[x][y][1] = 1;
      a[x][y] = '-';
      break;
    } else if (a[i][y] == '#') break;
  }

  for (int i = y-1; i >= 0; i--) {
    if (a[x][i] == '-' || a[x][i] == '|') {
      ban[x][y][2] = 1;
      a[x][y] = '|';
      break;
    } else if (a[x][i] == '#') break;
  }

  for (int i = y+1; i < c; i++) {
    if (a[x][i] == '-' || a[x][i] == '|') {
      ban[x][y][2] = 1;
      a[x][y] = '|';
      break;
    } else if (a[x][i] == '#') break;
  }

  return (ban[x][y][1] && ban[x][y][2]);
}

int cover(int x, int y, bool must = false) {
  int lx, ly;
  int dir;
  int opt = 0;
  for (int i = x+1; i < r; i++) {
    if (a[i][y] == '|' || a[i][y] == '-') {
      if (a[i][y] == '|' && ban[i][y][2]) {
        a[x][y] = 'c';
        return 1;
      } else if (!ban[i][y][1]) {
        opt++;
        lx = i, ly = y, dir = 1;
      }
      break;
    } else if (a[i][y] == '#') break;
  }

  for (int i = x-1; i >= 0; i--) {
    if (a[i][y] == '|' || a[i][y] == '-') {
      if (a[i][y] == '|' && ban[i][y][2]) {
        a[x][y] = 'c';
        return 1;
      } else if (!ban[i][y][1]) {
        opt++;
        lx = i, ly = y, dir = 1;
      }
      break;
    } else if (a[i][y] == '#') break;
  }

  for (int i = y-1; i >= 0; i--) {
    if (a[x][i] == '-' || a[x][i] == '|') {
      if (a[x][i] == '-' && ban[x][i][1]) {
        a[x][y] = 'c';
        return 1;
      } else if (!ban[x][i][2]) {
        opt++;
        lx = x, ly = i, dir = 2;
      }
      break;
    } else if (a[x][i] == '#') break;
  }

  for (int i = y+1; i < c; i++) {
    if (a[x][i] == '-' || a[x][i] == '|') {
      if (a[x][i] == '-' && ban[x][i][1]) {
        a[x][y] = 'c';
        return 1;
      } else if (!ban[x][i][2]) {
        opt++;
        lx = x, ly = i, dir = 2;
      }
      break;
    } else if (a[x][i] == '#') break;
  }

  assert(opt <= 2);
  if (opt == 0) return opt;
  if (!must && opt != 1) return opt;

  if (dir == 1) {
    a[lx][ly] = '|';
    ban[lx][ly][2] = 1;
  } else {
    a[lx][ly] = '-';
    ban[lx][ly][1] = 1;
  }

  return 1;
}

void solve(int casenum) {
  cout << "Case #" << casenum << ": ";
  cin >> r >> c;
  memset(ban, 0, sizeof(ban));
  FOR(i, r) {
    FOR(j, c) {
      cin >> a[i][j];
    }
  }

  FOR(i, r) {
    FOR(j, c) {
      if (a[i][j] == '|' || a[i][j] == '-') {
        bool rv = check(i, j);
        if (rv) {
          cout << "IMPOSSIBLE" << endl;
          return;
        }
      }
    }
  }

  set<pair<int, int> > rv2;
  while (1) {
    bool good = 0;
    FOR(i, r) {
      FOR(j, c) {
        if (a[i][j] == '.') {
          int rv = cover(i, j);
          if (rv == 0) {
            cout << "IMPOSSIBLE" << endl;
            return;
          }
          if (rv != 2) good = 1;
          if (rv == 2) rv2.insert(MP(i,j));
        }
      }
    }

    if (!good) break;
  }

  FOR(i, r) {
    FOR(j, c) {
      if (a[i][j] == '.' && rv2.find(MP(i,j)) == rv2.end()) {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
    }
  }

  // start solving

  while (1) {
    bool good = 0;
    FOR(i, r) {
      FOR(j, c) {
        if (a[i][j] == '.') {
          int rv = cover(i, j, true);
          if (rv == 0) {
            cout << "IMPOSSIBLE" << endl;
            return;
          }
          good = 1;
        }
      }
    }

    if (!good) break;
  }

  FOR(i, r) {
    FOR(j, c) {
      if (a[i][j] == '.') {
        cout << "IMPOSSIBLE" << endl;
        return;
      }
    }
  }

  cout << "POSSIBLE" << endl;
  FOR(i, r) {
    FOR(j, c) { if (a[i][j] == 'c') a[i][j] = '.'; cout << a[i][j]; }
    cout << endl;
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  FOR(tt,t) {
    solve(tt+1);
  }
  return 0;
}


