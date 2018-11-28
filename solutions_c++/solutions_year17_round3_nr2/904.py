#include <bits/stdc++.h>
using namespace std;

int c[105], d[105], j[105], k[105];

int main() {
  freopen("B-small-attempt2.in","r",stdin);
  freopen("B.out","w",stdout);
  int t;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    int ac, aj;
    scanf("%d%d", &ac, &aj);
    for (int j = 0; j < ac; j++) {
      scanf("%d%d", &c[j], &d[j]);
    }
    for (int tt = 0; tt < aj; tt++) {
      scanf("%d%d", &j[tt], &k[tt]);
    }
    sort(c, c + ac);
    sort(d, d + ac);
    sort(j, j + aj);
    sort(k, k + aj);
    int ret;
    if (ac + aj == 1) ret = 2;
    else if (ac == 1 && aj == 1) ret = 2;
    else {
      if (ac == 0) {
        if (j[1] - k[0] >= 720 || j[0] + 1440 - k[1] >= 720) ret = 2;
        else ret = 4;
      } else {
        if (c[1] - d[0] >= 720 || c[0] + 1440 - d[1] >= 720) ret = 2;
        else ret = 4;
      }
    }
    printf("%d\n", ret);
  }
}