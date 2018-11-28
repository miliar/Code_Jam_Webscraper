#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("C-small-2-attempt0.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    printf("Case #%d: ", tst);
    long long n, k;
    scanf("%lld %lld", &n, &k);
    priority_queue<long long> q;
    q.push(n);
    int cnt = 1;
    while (cnt < k && !q.empty()) {
      long long cur = q.top() - 1;
      q.pop();
      q.push(cur / 2);
      q.push((cur + 1) / 2);
      ++cnt;
    }
    n = q.top() - 1;
    printf("%lld %lld\n", (n + 1) / 2, n / 2);
    ++tst;
  }
}
