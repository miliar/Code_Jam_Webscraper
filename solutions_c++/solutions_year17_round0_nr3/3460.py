#include <cstdio>
#include <queue>
using namespace std;

int main() {
  int t, k, n, a, top;
  priority_queue<int> pq;

  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    scanf("%d %d", &n, &k);
    while (!pq.empty()) {
      pq.pop();
    }
    pq.push(n);
    while (--k) {
      top = pq.top();
      pq.pop();
      pq.push(top / 2);
      pq.push(top / 2 - !(top % 2));
    }
    top = pq.top();
    printf("Case #%d: %d %d\n", c, top / 2, top / 2 ? top / 2- !(top % 2) : 0);
  }
  return 0;
}
