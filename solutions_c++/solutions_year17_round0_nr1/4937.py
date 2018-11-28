#include <bits/stdc++.h>

using namespace std;

const int N = 1003;

char s[N];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    int k;
    scanf("%s %d", s, &k);
    int n = strlen(s), cnt = 0;
    bool possible = true;
    for (int i = 0; i < n; ++i) {
      if (s[i] == '-') {
        if (i + k > n) {
          possible = false;
          break;
        }
        for (int j = i; j < i + k; ++j) {
          s[j] = s[j] == '+' ? '-' : '+';
        }
        ++cnt;
      }
    }
    printf("Case #%d: ", tst);
    if (possible) {
      printf("%d\n", cnt);
    } else {
      puts("IMPOSSIBLE");
    }
    ++tst;
  }
}
