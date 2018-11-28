#include <bits/stdc++.h>
#define ll long long

using namespace std;

map <ll, int> m;

void io() {
  freopen("C-small-2-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

int main() {
  io();
  int test;
  scanf("%d", &test);
  for (int t = 1; t <= test; t++) {
    m.clear();
    ll n, k, p1 = 0, p2 = 0, cnt = 0;
    scanf("%I64d %I64d", &n, &k);
    queue <ll> q;
    q.push(n);
    m[n] = 1;
    while ((! q.empty()) && (cnt < k)) {
      ll use = q.front();
      cnt += m[use];
      q.pop();
      p1 = use / 2;
      p2 = use - p1 - 1;
      if (! m[p1]) {
        q.push(p1);
      }
      m[p1] += m[use];
      if (! m[p2]) {
        q.push(p2);
      }
      m[p2] += m[use];
      if (p1 == 0 && p2 == 0) {
        break;
      }
    }
    if (p1 < p2) {
      swap(p1, p2);
    }
    printf("Case #%d: %I64d %I64d\n", t, p1, p2);
  }
  return 0;
}
