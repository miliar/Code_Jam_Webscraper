#include <cstdio>
#include <queue>
#include <map>

using namespace std;

map<long long, long long> mm;
priority_queue<long long> q;

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/C-large.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/cl.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  long long n, k;
  while (T--) {
    scanf("%lld%lld", &n, &k);
    while (!q.empty()) q.pop();
    mm.clear();
    long long need = k;
    q.push(n);
    mm[n] = 1;
    long long l, r;
    while (need > 0) {
      long long x = q.top();
      need -= mm[x];
      q.pop();
      l = x / 2;
      r = (x - 1) / 2;
      if (x & 1) {
        if (mm.find(l) == mm.end()) {
          mm[l] = 0;
          q.push(l);
        }
        mm[l] += 2 * mm[x];
      } else {
        if (mm.find(l) == mm.end()) {
          mm[l] = 0;
          q.push(l);
        }
        mm[l] += mm[x];
        if (mm.find(r) == mm.end()) {
          mm[r] = 0;
          q.push(r);
        }
        mm[r] += mm[x];
      }
    }
    printf("Case #%d: %lld %lld\n", ++tc, l, r);
  }
  return 0;
}