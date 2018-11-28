#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pi;

const int N = 1010;

int n, c, m;
int cnt[N];
int a[N];

pair<bool, int> check(int u) {
  int res = 0;
  int foo = 0;
  for (int i = n; i; i--) {
    int bar = foo + a[i];
    if (bar <= u) {
      foo = 0;
      continue;
    }
    int need = bar - u;
    res += max(0, need - foo);
    foo = need;
  }
  if (foo > 0) {
    return pi(0, 0);
  }
  return pi(1, res);
}

pair<int, int> solver() {
  scanf("%d %d %d", &n, &c, &m);
  for (int i = 1; i <= c; i++) {
    cnt[i] = 0;
  }
  for (int i = 1; i <= n; i++) {
    a[i] = 0;
  }
  for (int i = 1; i <= m; i++) {
    int u;
    scanf("%d", &u);
    a[u]++;
    scanf("%d", &u);
    cnt[u]++;
  }
  int low = 0;
  for (int i = 1; i <= c; i++) {
    low = max(low, cnt[i]);
  }
  low--;
  int high = m + 1;
  while (high - low > 1) {
    int mid = (low + high) >> 1;
    if (check(mid).first) {
      high = mid;
    } else {
      low = mid;
    }
  }
  return pi(high, check(high).second);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tc;
  scanf("%d", &tc);
  for (int i = 1; i <= tc; i++) {
    pair<int, int> res = solver();
    printf("Case #%d: %d %d\n", i, res.first, res.second);
  }
  return 0;
}
