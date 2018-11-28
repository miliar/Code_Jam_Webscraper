#include <cstdio>
#include <queue>

using namespace std;

int T, tt;
int n, k;
priority_queue<int> q;

void solve() {
  scanf("%d %d", &n, &k);
  while(! q.empty())
    q.pop();
  q.push(n);
  for(int i = 1; i < k; i++) {
    int m = q.top(); q.pop();
    m--;
    q.push(m / 2);
    q.push(m / 2 + m % 2);
  }
  int m = q.top(); q.pop();
  m--;
  printf("%d %d\n", (m / 2 + m % 2), (m / 2));
}

int main() {
  scanf("%d", &T);
  for(tt = 1; tt <= T; tt++) {
    printf("Case #%d: ", tt);
    solve();
  }
  return 0;
}
