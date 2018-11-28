/*input
1
+-+- 2
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc)
  {
    char s[1004];
    int k;
    scanf("%s %d\n", s, &k);
    printf("Case #%d: ", tc);

    int n = strlen(s), cnt = 0;
    for (int i = 0; i < n; ++i)
    {
      s[i] = s[i] == '-';
      cnt += s[i];
    }

    if (cnt & 1 == k & 1) {
      puts("IMPOSSIBLE");
    }

    int ans = 0;
    for (int i = 0; i <= n-k && cnt; ++i)
    {
      if (!s[i]) continue;
      
      ans++;
      int sum = 0;
      for (int j = 0; j < k; ++j)
      {
        sum += s[i + j];
        s[i + j] ^= 1;
      }
      cnt += k - 2 * sum;
    }

    if (cnt) {
      puts("IMPOSSIBLE");
    } else {
      printf("%d\n", ans);
    }
  }
  return 0;
}