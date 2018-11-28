#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

void flip(char *s, int l, int r) {
  for (int i = l; i <= r; ++i) {
    s[i] = '+' + '-' - s[i];
  }
}

void go(char *s, int k) {
  int n = strlen(s);
  int c = 0;
  for (int i = 0; i < n; ++i) {
    if (s[i] == '-') {
      if (i + k - 1 < n) {
        flip(s, i, i + k - 1);
        ++c;
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    if (s[i] == '-') {
      puts("IMPOSSIBLE");
      return;
    }
  }
  printf("%d\n", c);
}

int main() {
  int t;
  scanf("%d", &t);
  char s[N];
  int k;
  for (int _ = 1; _ <= t; ++_) {
    scanf("%s%d", s, &k);
    printf("Case #%d: ", _);
    go(s, k);
  }
  return 0;
}
