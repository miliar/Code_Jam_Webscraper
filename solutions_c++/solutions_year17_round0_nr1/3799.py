#include <bits/stdc++.h>

using namespace std;

const int N = 1234;

char s[N];

void io() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

int len(char a[]) {
  int ret = 0;
  while (a[ret] != '\0') {
    ret++;
  }
  return ret;
}

int main() {
  io();
  int test, k, ans, flag, n;
  scanf("%d", &test);
  for (int t = 1; t <= test; t++) {
    scanf("%s", s);
    scanf("%d", &k);
    n = len(s);
    ans = flag = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == '-' && (n - i) >= k) {
        for (int j = 0; j < k; j++) {
          s[i + j] = (s[i + j] == '-') ? '+' : '-';
        }
        ans++;
      }
      if (s[i] == '-') {
        flag = 1;
        break;
      }
    }
    printf("Case #%d: ", t);
    if (! flag) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
  return 0;
}
