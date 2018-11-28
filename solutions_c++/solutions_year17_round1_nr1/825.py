#include <bits/stdc++.h>
using namespace std;

int T, R, C;
char m[30][30];
bool k[30][30];

void fill(int a, int b) {
  int left = b, right = b, up = a, down = a, f;
  while (left > 0) {
    if (m[a][left-1] == '?') left--;
    else break;
  }
  while (right < C-1) {
    if (m[a][right+1] == '?') right++;
    else break;
  }
  f = 1;
  while (up > 0 && f) {
    for (int i = left; i <= right && f; i++) {
      if (m[up-1][i] == '?') continue;
      f = 0;
    }
    if (f) up--;
  }
  f = 1;
  while (down < R-1 && f) {
    for (int i = left; i <= right && f; i++) {
      if (m[down+1][i] == '?') continue;
      f = 0;
    }
    if (f) down++;
  }
  for (int i = up; i <= down; i++) {
    for (int j = left; j <= right; j++) {
      m[i][j] = m[a][b];
      k[i][j] = 0;
    }
  }
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &R, &C);
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        k[i][j] = 1;
      }
    }
    for (int i = 0; i < R; i++) {
      scanf("%s", m[i]);
    }
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        if (m[i][j] != '?' && k[i][j]) {
          fill(i, j);
        }
      }
    }
    printf("Case #%d:\n", t);
    for (int i = 0; i < R; i++) {
      printf("%s\n", m[i]);
    }
  }
  return 0;
}

