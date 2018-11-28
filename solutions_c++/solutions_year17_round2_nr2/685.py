#include <stdio.h>

int main() {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int n, r, o, y, g, b, v;
    scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
    bool impossible = false;
    char answer[100000];
    int a = 0;
    if (r >= y && r >= b) {
      while (r > 0) {
        answer[a++] = 'R';
        r--;
        if (y >= b) {
          answer[a++] = 'Y';
          y--;
        } else {
          answer[a++] = 'B';
          b--;
        }
      }
      while (y > 0 || b > 0) {
        if (y >= b) {
          answer[a++] = 'Y';
          y--;
        } else {
          answer[a++] = 'B';
          b--;
        }
      }
      if (y < 0 || b < 0)
        impossible = true;
    } else if (y >= r && y >= b) {
      while (y > 0) {
        answer[a++] = 'Y';
        y--;
        if (r >= b) {
          answer[a++] = 'R';
          r--;
        } else {
          answer[a++] = 'B';
          b--;
        }
      }
      while (r > 0 || b > 0) {
        if (r >= b) {
          answer[a++] = 'R';
          r--;
        } else {
          answer[a++] = 'B';
          b--;
        }
      }
      if (r < 0 || b < 0)
        impossible = true;
    } else {
      while (b > 0) {
        answer[a++] = 'B';
        b--;
        if (r >= y) {
          answer[a++] = 'R';
          r--;
        } else {
          answer[a++] = 'Y';
          y--;
        }
      }
      while (r > 0 || y > 0) {
        if (r >= y) {
          answer[a++] = 'R';
          r--;
        } else {
          answer[a++] = 'Y';
          y--;
        }
      }
      if (r < 0 || y < 0)
        impossible = true;
    }
    answer[a++] = '\0';
    if (impossible)
      sprintf(answer, "IMPOSSIBLE");
    printf("Case #%d: %s\n", t, answer);
  }
  return 0;
}
