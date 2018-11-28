#include <cstdio>
#include <cassert>
#include <cmath>
#include <set>
#include <vector>
#include <cstring>


using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

vector <int> a{1, 3, 2, 6, 4, 5};
vector <char> b{'R', 'O', 'Y', 'G', 'B', 'V'};
vector <int> res;
int n;

set<pair<vector<int>, int>> used;
vector<int> t(6);

int go(int ind) {
  if (used.size() > 1e6) return 0;
  if (ind == n) {
    return (a[res[0]] & a[res[n - 1]]) == 0;
  }
  auto c = make_pair(t, res[ind - 1]);
  if (used.count(c)) return 0;
  used.insert(c);
  vector<int> p(6);
  for (int i = 0; i < 6; i++) p[i] = i;
  sort(p.begin(), p.end(), [&](int x, int y) { return t[x] > t[y];});
  for (int q = 0; q < 6; q++) {
    int i = p[q];
    if (t[i] > 0 && (a[res[ind - 1]] & a[i]) == 0) {
      t[i]--;
      res[ind] = i;
      int f = go(ind + 1);
      if (f) return 1;
      t[i]++;
    }
  }
  return 0;
}

void solve() {
  scanf("%d", &n);
  used.clear();
  for (int i = 0; i < 6; i++) scanf("%d", &t[i]);
  res = vector<int>(n);
  int f;
  for (int i = 0; i < 6; i++) {
    if (t[i] > 0) {
      t[i]--;
      res[0] = i;
      f = go(1);
    }
  }
  if (f == 0) {
    printf("IMPOSSIBLE\n");
  } else {
    for (int i = 0; i < n; i++) printf("%c", b[res[i]]);
    printf("\n");
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    printf("Case #%d: ", test);
    solve();
    eprintf("passed %d\n", test);
    fflush(stdout);
  }
}
