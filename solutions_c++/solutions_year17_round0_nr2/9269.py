#include <bits/stdc++.h>
using namespace std;

int main () {
  int tc, x = 1;
  long long ans;
  for (scanf("%d", &tc); tc--; printf("Case #%d: %lld\n", x++, ans)) {
    long long in;
    scanf("%lld", &in);
    long long pew[20] = {1};
    for (int i = 1; i < 18; i++) pew[i] = pew[i - 1] * 10;
    while (true) {
      // printf("%lld %lld\n", ans, in);
      char conv[20];
      long long temp = in;
      int n = 0;
      // printf("--%d %lld\n", n, temp);
      while (temp) {
        // printf("%d %lld\n", n, temp);
        conv[n] = temp % 10;
        conv[n] += '0';
        temp /= 10;
        n++;
      }
      conv[n] = '\0';
      for (int i = 0; i < n / 2; i++) {
        swap(conv[i], conv[n - i - 1]);
      }
      // printf("%s\n", conv);

      ans = 0;
      ans = (conv[0] - '0') * pew[n - 1];
      int i;
      for (i = 1; i < n; i++) {
        if (conv[i - 1] > conv[i]) break;
        ans += (conv[i] - '0') * pew[n - i - 1];
      }
      if (i < n) ans--;

      bool flag = 1;
      for (int i = 0; i < n - 1; i++) {
        if (conv[i] > conv[i + 1]) {
          flag = 0;
          break;
        }
      }

      in = ans;
      // break;
      if (flag) break;
    }
  }

  return 0;
}
