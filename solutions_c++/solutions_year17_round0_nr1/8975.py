#include <bits/stdc++.h>
using namespace std;

int main () {
  int tc, x = 1;
  for (scanf("%d", &tc); tc--; ) {
    char in[1002];
    scanf("%s", in);
    int k;
    scanf("%d", &k);

    int n = strlen(in);
    int ans = 0;
    for (int i = 0; i < n - k + 1; i++) {
      if (in[i] == '+') continue;

      ans++;
      for (int j = i; j < i + k; j++) {
        in[j] = in[j] == '+' ? '-' : '+';
      }
    }

    bool flag = 1;
    for (int i = 0; i < n; i++) {
      if (in[i] == '-') {
        flag = 0;
        break;
      }
    }

    printf("Case #%d: ", x++);
    if (flag) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }

  return 0;
}
