#define NDEBUG
#include <cstring>
#include <functional>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

#define MINUSONE(v) memset((v), -1, sizeof (v))
#define ZERO(v) memset((v), 0, sizeof (v))
#define repeat(n) for (int repc = (n); repc > 0; --repc)

const int MAXN = 205;

struct Matching {
  int n;
  bool graf[MAXN][MAXN];
  bool vism[MAXN];
  int parf[MAXN];
  bool dfs(int v) {
    if (vism[v]) {
      return false;
    }
    vism[v] = 1;
    for (int j=0; j<n; ++j) {
      if (graf[v][j] &&
          (parf[j] == -1 || dfs(parf[j]))) {
        parf[j] = v;
        return true;
      }
    }
    return false;
  }

  int matching() {
    int rez = 0;
    MINUSONE(parf);
    for (int v=0; v<n; ++v) {
      ZERO(vism);
      if (dfs(v)) {
        ++rez;
      }
    }
    return rez;
  }
};

void solve() {
  int N, pre;
  cin >> N >> pre;
  Matching cross, diag;

  cross.n = N;
  memset(cross.graf, 1, sizeof(cross.graf));

  diag.n = 2 * N - 1;
  ZERO(diag.graf);
  for (int y = 0; y < N; ++y) {
    for (int x = 0; x < N; ++x) {
      int d1 = y + x, d2 = N - 1 + y - x;
      diag.graf[d1][d2] = 1;
    }
  }

  static char input[MAXN][MAXN];
  memset(input, '.', sizeof(input));
  repeat (pre) {
    char ch; int y, x;
    cin >> ws >> ch >> y >> x;
    --y; --x;
    input[y][x] = ch;
    if (ch == 'o' || ch == '+') {
      int d1 = y + x, d2 = N - 1 + y - x;
      for (int i = 0; i < 2 * N - 1; ++i) {
        diag.graf[d1][i] = 0;
        diag.graf[i][d2] = 0;
      }
      diag.graf[d1][d2] = 1;
    }
    if (ch == 'o' || ch == 'x') {
      for (int i = 0; i < N; ++i) {
        cross.graf[y][i] = 0;
        cross.graf[i][x] = 0;
      }
      cross.graf[y][x] = 1;
    }
  }

  cross.matching();
  diag.matching();
  int pts = 0;
  vector<tuple<char, int, int> > out;
  for (int y = 0; y < N; ++y) {
    for (int x = 0; x < N; ++x) {
      int d1 = y + x, d2 = N - 1 + y - x;
      bool plus = diag.parf[d2] == d1;
      bool ex = cross.parf[x] == y;
      char ch = plus && ex ? 'o' : plus ? '+' : ex ? 'x' : '.';
      if (ch != input[y][x]) {
        out.emplace_back(ch, y + 1, x + 1);
      }
      pts += plus;
      pts += ex;
    }
  }
  cout << pts << ' ' << out.size() << '\n';
  for (const auto& tup : out) {
    cout << get<0>(tup) << ' ' << get<1>(tup) << ' ' << get<2>(tup) << '\n';
  }
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": ";
    solve();
  }
}
