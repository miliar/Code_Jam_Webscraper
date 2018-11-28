#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 1010;

char s[N];

inline void change(int x, int y) {
  for (int i = x; i <= x + y - 1; i++) {
    if (s[i] == '+') {
      s[i] = '-';
    } else {
      s[i] = '+';
    }
  }
}

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int k;
    scanf("\n%s %d", s + 1, &k);
    int n = strlen(s + 1);
    int res = 0;
    for (int i = 1; i <= n - k + 1; i++) {
      if (s[i] == '-') {
        change(i, k);
        ++res;
      }
    }
    bool checked = false;
    for (int i = n - k + 2; i <= n; i++) {
      if (s[i] == '-') {
        checked = true;
      }
    }
    if (checked) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", res);
    }
  }
  return 0;
}