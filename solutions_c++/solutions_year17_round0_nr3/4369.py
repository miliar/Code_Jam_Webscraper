#include <bits/stdc++.h>
using namespace std;
int main() {
  int T, n, k;
  scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) {
    scanf("%d%d", &n, &k);
    priority_queue<int> q;
    q.push(n);
    for (int i = 0; i < k - 1; ++ i) {
      int u = q.top();
      q.pop();
      q.push((u + 1) / 2 - 1);
      q.push(u - (u + 1) / 2);
    }
    int u = q.top();
    printf("Case #%d: %d %d\n", cas, max((u + 1) / 2 - 1, u - (u + 1) / 2), min((u + 1) / 2 - 1, u - (u + 1) / 2));
  }
  return 0;
}
