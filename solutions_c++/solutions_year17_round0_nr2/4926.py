#include <bits/stdc++.h>

using namespace std;

const int N = 1003;

char s[N];

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t, tst = 1;
  scanf("%d", &t);
  while (t--) {
    printf("Case #%d: ", tst);
    long long n;
    scanf("%lld", &n);
    long long x = n;
    int nines = 0, cnt = 0;
    while (n > 0) {
      int d = n % 10;
      int dd = (n % 100) / 10;
      if (dd > d) {
        x = n / 100 * 10 + dd - 1; // 1 20 0
        nines = cnt + 1;
        n = x * 10;
      }
      ++cnt;
      n /= 10;
    }
    while (nines--) {
      x *= 10;
      x += 9;
    }
    printf("%lld\n", x);
    ++tst;
  }
}
