#include <cstdio>
#include <cstring>
#include <algorithm>
#define i64 long long
using namespace std;

const int N = 1e3 + 10;
int T, cnt;
i64 n, k;

struct node {
      i64 v, n;
      bool operator < (node const & x) const {
            return v > x.v;
      }
} p[N];

void add(i64 v, i64 n) {
      for (int i = 1;  i <= cnt; ++ i) if (p[i].v == v) {
            p[i].n += n;
            return;
      }
      p[++ cnt] = (node) {v, n};
}

int main() {
      freopen("c.in", "r", stdin);
      freopen("c.out", "w", stdout);
      scanf("%d", &T);
      for (int t = 1; t <= T; ++ t) {
            scanf("%lld %lld", &n, &k);
            k --;
            printf("Case #%d: ", t);
            p[cnt = 1] = (node) {n, 1};
            for (; ;) {
                  sort(p + 1, p + cnt + 1);
                  i64 v = p[1].v, n = p[1].n;
                  if (n > k) {
                        printf("%lld %lld\n", v / 2, (v - 1) / 2);
                        break;
                  }
                  k -= n;
                  i64 a1 = (v - 1) / 2;
                  i64 a2 = v - 1 - a1;
                  add(a1, n), add(a2, n);
                  p[1] = (node) {0, 0};
            }

      }
      return 0;
}
