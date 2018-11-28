#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>

#define pb push_back
#define mp make_pair

#define f first
#define s second

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

const int N = (int) 1e6 + 7;
const int MOD = (int) 1e9 + 7;

const int SQRT = (int) 320;

int n, c, m;
int cnt[N];
vector<int> tickets[N];

int check(int rides) {
  for (int i = 1; i <= n; i++)
    cnt[i] = rides;

  for (int who = 1; who <= c; who++)
    if ((int) tickets[who].size() > rides)
      return -1;

  int changes = 0;
  for (int who = 1; who <= c; who++) {
    for (auto place : tickets[who]) {
      int sitIn = place;
      if (!cnt[sitIn]) {
        while (sitIn > 0 && !cnt[sitIn]) --sitIn;
        changes++;
        if (sitIn == 0)
          return -1;
      }
      cnt[sitIn]--;
    }
  }
  return changes;
}

void solve() {
  scanf("%d%d%d", &n, &c, &m);
  for (int i = 1; i <= c; i++)
    tickets[i].clear();
  for (int i = 1; i <= m; i++) {
    int a, b;
    scanf("%d%d", &a, &b);
    tickets[b].pb(a);
  }
  int l = 1, r = m, ans = m;
  while (l <= r) {
    int mid = (l + r) / 2;
    if (check(mid) != -1) {
      ans = mid;
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }
  printf("%d %d\n", ans, check(ans));
}

int main() {
  #ifdef LOCAL
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif

  int t; scanf("%d", &t);
  for (int tcase = 1; tcase <= t; tcase++) {
    printf("Case #%d: ", tcase);
    solve();
    cerr << tcase << " is done\n";
  }


  return 0;
}