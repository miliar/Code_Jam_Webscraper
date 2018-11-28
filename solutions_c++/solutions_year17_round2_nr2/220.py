#include <bits/stdc++.h>

using namespace std;

//#define SMALL
#define LARGE

struct Color {
  char c;
  int x;
  
  bool operator < (const Color& other) const {
    return x < other.x;
  }
} color[10];

int n, r, o, y, g, b, v;
int ans[1005];

int main()
{
#ifdef SMALL
  freopen("B-small.in", "r", stdin);
  freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  for (int Case = 1; Case <= T; ++Case) {
    scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
    printf("Case #%d: ", Case);
    if (r + g == n && r == g) {
      for (int i = 0; i < r; ++i)
        printf("RG");
      printf("\n");
      continue;
    }
    if (y + v == n && y == v) {
      for (int i = 0; i < y; ++i)
        printf("YV");
      printf("\n");
      continue;
    }
    if (b + o == n && b == 0) {
      for (int i = 0; i < b; ++i)
        printf("BO");
      printf("\n");
      continue;
    }
    bool isans = true;
    if (b > o || o == 0)
      b -= o, n -= 2 * o;
    else
      isans = false;
    if (y > v || v == 0)
      y -= v, n -= 2 * v;
    else
      isans = false;
    if (r > g || g == 0)
      r -= g, n -= 2 * g;
    else
      isans = false;
    color[0].x = r; color[0].c = 'R';
    color[1].x = y; color[1].c = 'Y';
    color[2].x = b; color[2].c = 'B';
    sort(color, color + 3);
    if (n / 2 < color[2].x || !isans) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    bool dov = false, doo = false, dog = false;
    memset(ans, -1, sizeof(ans));
    for (int i = 0; i < color[2].x; ++i)
      ans[i << 1] = 2;
    for (int i = 0; i < color[1].x; ++i)
      ans[n - (i << 1) - (n & 1) - 1] = 1;
    for (int i = 0; i < n; ++i)
      if (ans[i] == -1)
        ans[i] = 0;
    for (int i = 0; i < n; ++i) {
      printf("%c", color[ans[i]].c);
      if (color[ans[i]].c == 'Y' && !dov) {
        dov = true;
        for (int j = 0; j < v; ++j)
          printf("VY");
      }
      if (color[ans[i]].c == 'B' && !doo) {
        doo = true;
        for (int j = 0; j < o; ++j)
          printf("OB");
      }
      if (color[ans[i]].c == 'R' && !dog) {
        dog = true;
        for (int j = 0; j < g; ++j)
          printf("GR");
      }
    }
    printf("\n");
  }
  return 0;
}
