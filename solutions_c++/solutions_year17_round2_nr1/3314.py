#include <iostream>
#include <algorithm>

int main(void)
{
  int t, n, s;
  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    int k, d;
    scanf("%d %d", &s, &n);
  
    long double res = 1000000000000000000.0;
    for (int i = 0; i < n; ++i) {
      scanf("%d %d", &k, &d);
      res = std::min(res, static_cast<long double>(s) / ((static_cast<long double>(s) - static_cast<long double>(k)) / static_cast<long double>(d)));
    }

    printf("Case #%d: %Lf\n", test, res);
  }

  return 0;
}