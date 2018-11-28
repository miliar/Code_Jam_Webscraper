#include <bits/stdc++.h>

using namespace std;

#define SMALL
//#define LARGE

int num[5];

int main()
{
#ifdef SMALL
  freopen("A-small.in", "r", stdin);
  freopen("A-small.out", "w", stdout);
#endif
#ifdef LARGE
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  for (int Case = 1; Case <= T; ++Case) {
    memset(num, 0, sizeof(num));
    int n, p;
    scanf("%d %d", &n, &p);
    int x;
    for (int i = 0; i < n; ++i) {
      scanf("%d", &x);
      x %= p;
      ++num[x];
    }
    printf("Case #%d: ", Case);
    if (p == 2) {
      printf("%d\n", num[0] + (num[1] + 1) / 2);
      continue;
    }
    int ans = num[0];
    int temp = min(num[1], num[2]);
    ans += temp;
    num[1] -= temp; num[2] -= temp;
    ans += (num[2] + 2) / 3 + (num[1] + 2) / 3;
    printf("%d\n", ans);
  }
  return 0;
}
