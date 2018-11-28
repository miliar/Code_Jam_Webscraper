#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

char S[30000];
int a[3000];
int k;

int main() {
  ios ::sync_with_stdio(0);
  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> S >> k;

    memset(a, 0, sizeof(a));

    int cnt = 0;

    bool good = true;
    int n = strlen(S);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
      if (i - k >= 0) {
        cnt -= a[i - k];
      }

      if (i + k <= n) {
        if ((S[i] == '-' && cnt % 2 == 0) || (S[i] == '+' && cnt % 2 == 1)) {
          a[i] = 1;
          cnt++;
          ans++;
        }
      } else {
        if ((S[i] == '-' && cnt % 2 == 0) || (S[i] == '+' && cnt % 2 == 1)) {
          good = false;
          break;
        }
      }
    }

    printf("Case #%d: ", cn);
    if (!good)
      printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
  }
  return 0;
}
