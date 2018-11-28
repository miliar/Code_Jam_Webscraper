#include <bits/stdc++.h> 

using namespace std;

const int N = 1010;

char s[N];
int t, cs = 0, n, k;

int main (int argc, char const *argv[]) {
  scanf("%d", &t); while (t--) {
    scanf("%s %d", s + 1, &k);
    n = strlen(s + 1);
    int moves = 0;
    for (int i = 1; i <= n - k + 1; ++i) {
      if (s[i] == '-') {
        ++moves;
        for (int j = i; j < i + k; ++j) {
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
      }
    }
    bool flag = 1;
    for (int i = 1; i <= n; ++i) {
      if (s[i] == '-') {
        flag = 0;
        break;
      }
    }
    printf("Case #%d: ", ++cs);
    if (flag) printf("%d\n", moves);
    else puts("IMPOSSIBLE");
  }
  return 0;
}

