#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1e3 + 10;
int T, k, l, ans, flg;
char s[N];

int main() {
      freopen("a.in", "r", stdin);
      freopen("a.out", "w", stdout);
      scanf("%d", &T);
      for (int t = 1; t <= T; ++ t) {
            scanf("%s", s + 1);
            scanf("%d", &k);
            l = strlen(s + 1);
            flg = ans = 0;
            for (int i = 1; i <= l; ++ i) if (s[i] == '-') {
                  ans ++;
                  if (i + k - 1 > l) {
                              flg = 1;
                              break;
                  }
                  for (int j = i; j <= i + k - 1; ++ j)
                  if (s[j] == '+') s[j] = '-'; else s[j] = '+';
            }
            printf("Case #%d: ", t);
            if (flg) printf("IMPOSSIBLE\n");
            else printf("%d\n", ans);
      }
      return 0;
}
