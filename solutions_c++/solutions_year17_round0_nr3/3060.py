#include <cstdio>
#include <cmath>
#include <cstdint>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

unordered_map<int64_t, int64_t> m;

void add(priority_queue<int64_t> & q, int64_t width, int64_t n) {
  if (m.find(width) == m.end()) {
    m[width] = n;
    q.push(width);
  } else {
    m[width] += n;
  }
}

int main() {
  int t;
  scanf("%d\n", &t);
  for (int it=1; it<=t; ++it) {
    priority_queue<int64_t> q;
    m.clear();
    int64_t n, k, rmax = 0, rmin = 0;
    scanf("%lld%lld", &n, &k);
    q.push(n);
    m[n] = 1;
    while (k > 0) {
      int64_t largest = q.top();
      q.pop();
      int64_t stalls = m[largest];
      m.erase(largest);
      if (stalls < k) {
        // let m[largest] people in
        int64_t half = (largest - 1)/2;
        add(q, half, stalls);
        add(q, largest - half - 1, stalls);
        k -= stalls;
        continue;
      }
      rmin = (largest - 1)/2;
      rmax = largest - rmin - 1;
      break;
    }
    printf("Case #%d: %lld %lld\n", it, rmax, rmin);
  }
}
