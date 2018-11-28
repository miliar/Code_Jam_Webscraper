#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <cstdlib>

using namespace std;

bool vis[1010];
bool has[1010];
int cnt[1010];

struct P {
  int seat, id;

  bool operator<(const P &p) const {
    if (seat != p.seat) return seat < p.seat;
    return id < p.id;
  }
} tic[1010];

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/B-small-attempt0.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/B-small.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    int ans1 = 0, ans2, tot = 0;
    int n, m, c;
    scanf("%d%d%d", &n, &c, &m);
    memset(cnt, 0, sizeof(cnt));
    memset(vis, 0, sizeof(vis));
    for (int i = 0; i < m; ++i) {
      scanf("%d%d", &tic[i].seat, &tic[i].id);
      ++cnt[tic[i].seat];
    }

    sort(tic, tic + m);


    while (tot < m) {
      ++ans1;
      memset(has, 0, sizeof(has));
      int cur = 1;
      for (int i = 0; i < m; ++i) {
//        printf("ente i = %d\n", i);
        if (vis[i] || has[tic[i].id] || tic[i].seat < cur) continue;
        vis[i] = 1;
        has[tic[i].id] = 1;
        ++cur;
        ++tot;
//        printf("tot=%d\n", tot);
      }
    }

//    printf("ans1=%d\n", ans1);

    ans2 = 0;
    for (int i = 1; i <= n; ++i) {
      ans2 += max(cnt[i] - ans1, 0);
    }
    printf("Case #%d: %d %d\n", ++tc, ans1, ans2);
  }
  return 0;
}