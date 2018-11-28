#include <cstdio>
#include <map>
#include <queue>


const int MAXP = 100;

using namespace std;

#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

void solve() {
  int Hd, Ad, Hk, Ak, B, D;
  scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
  queue<pair<pair<int, int>, pair<int, int>>> pq;
  map<pair<pair<int, int>, pair<int, int>>, int> d;
  auto s = mp(mp(Hd, Ad), mp(Hk, Ak));
  d[s] = 0;
  pq.push(s);
  int flag = 0;
  while (!pq.empty()) {
    auto cur = pq.front();
    pq.pop();
    //eprintf("(%d, %d), (%d, %d) %d\n", cur.first.first, cur.first.second, cur.second.first, cur.second.second, d[cur]);
    if (cur.second.first <= 0) {
      printf("%d\n", d[cur]);
      flag = 1;
      break;
    }
    if (cur.first.first <= 0) continue;
    auto t1 = cur;
    t1.first.second = min(t1.first.second + B, MAXP);
    t1.first.first -= t1.second.second;
    auto t2 = cur;
    t2.second.second = max(0, t2.second.second - D);
    t2.first.first -= t2.second.second;
    auto t3 = cur;
    t3.first.first = Hd;
    t3.first.first -= t3.second.second;
    auto t4 = cur;
    t4.second.first -= t4.first.second;
    t4.first.first -= t4.second.second;
    if (!d.count(t1)) {
      pq.push(t1);
      d[t1] = d[cur] + 1;
    }
    if (!d.count(t2)) {
      pq.push(t2);
      d[t2] = d[cur] + 1;
    }
    if (!d.count(t3)) {
      pq.push(t3);
      d[t3] = d[cur] + 1;
    }
    if (!d.count(t4)) {
      pq.push(t4);
      d[t4] = d[cur] + 1;
    }
  }
  if (!flag) {
    printf("IMPOSSIBLE\n");
  }
}
int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    printf("Case #%d: ", test);
    solve();
  }
}
