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

int n, p;
LL r[50];
LL x;
vector<LL> q[50];
int idx[50];
LL cnt = 0;
LL nxt;

int chosen[50];
bool take(LL port) {
  FOR(i, n) {
    chosen[i] = -1;
    for (int j = idx[i]; j < p; j++) {
      if (r[i] * port * 9 <= q[i][j] * 10 && q[i][j] * 10 <= r[i] * port * 11) {
        chosen[i] = j;
        break;
      }
    }
    if (chosen[i] == -1) return false;
  }

  //cout << "FOUND " << port << endl;

  cnt++;
  FOR(i, n) {
    idx[i] = chosen[i] + 1;
  }
  return true;
}

bool isgood() {
  FOR(i, n) if (idx[i] >= p) return false;
  FOR(i, n) if (q[i][p - 1] * 10 < r[i] * nxt * 9) return false;
  return true;
}

void solve(int tc) {
  cout << "Case #" << tc << ": ";
  cnt = 0;
  cin >> n >> p;
  FOR(i, n) {
    cin >> r[i];
  }
  FOR(i, n) {
    q[i].clear();
    FOR(j, p) {
      cin >> x;
      q[i].push_back(x);
    }
    sort(q[i].begin(), q[i].end());
    idx[i] = 0;
  }
  nxt = 1;
  while (isgood()) {
    bool rv = take(nxt);
    if (!rv) nxt++;
  }

  cout << cnt << endl;
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


