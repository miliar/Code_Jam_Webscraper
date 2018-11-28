#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

char pancake[N];

int main() {
  int t, k;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; tc++) {
    scanf("%s %d", pancake, &k);
    int n = strlen(pancake), ans = 0;
    for (int i = 0; i < n; i++) {
      if (pancake[i] == '-' and i + k <= n) {
        for (int j = i; j < i + k; j++) {
          if (pancake[j] == '+') {
            pancake[j] = '-';
          } else {
            pancake[j] = '+';
          }
        }
        ++ans;
      }
    }
    bool has = true;
    for (int i = 0; i < n; i++) {
      if (pancake[i] == '-') {
        has = false;
        break;
      }
    }
    printf("Case #%d: ", tc);
    if (has) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
  return 0;
}