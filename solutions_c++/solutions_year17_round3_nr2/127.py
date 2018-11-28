#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 200, INF = 987654321;
int d[2222], e[2222];

struct Data {
  int s, e, t;
  bool operator < (const Data &rhs) const {
    return s < rhs.s;
  }
} a[N];

int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int ac, aj;
    scanf("%d%d", &ac, &aj);
    for (int i = 0; i < ac; ++i) {
      scanf("%d%d", &a[i].s, &a[i].e);
      a[i].t = 0;
    }
    for (int i = ac; i < ac + aj; ++i) {
      scanf("%d%d", &a[i].s, &a[i].e);
      a[i].t = 1;
    }
    sort(a, a + ac + aj);
    int rc = 720, rj = 720, dn = 0;
    d[0] = 0;
    for (int i = 0; i < ac + aj; ++i) {
      if (a[i].t == 0) rj -= a[i].e - a[i].s;
      else             rc -= a[i].e - a[i].s;
      int j = (i + 1) % (ac + aj);
      int ln = (a[j].s - a[i].e + 1440) % 1440;
      for (int k = 0; k <= dn + ln; ++k) e[k] = INF;
      for (int k = 0; k <= dn; ++k) {
        for (int l = 0; l <= ln; ++l) {
          int c = 1;
          if (a[i].t == a[j].t) {
            if (a[i].t == 0 && l == 0) c = 0;
            else if (a[i].t == 1 && l == ln) c = 0;
            else c = 2;
          }
          e[k + l] = min(e[k + l], d[k] + c);
        }
      }
      dn += ln;
      for (int k = 0; k <= dn; ++k) {
        d[k] = e[k];
      }
    }
    printf("Case #%d: %d\n", ti + 1, d[rc]);
  }
  return 0;
}
