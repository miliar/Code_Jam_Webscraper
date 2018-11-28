#include <iostream>
#include <algorithm>
#include <tuple>
#include <vector>

#define PI (3.14159265358979323846264338327950288419)

int main(void)
{
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    int n, k;
    scanf("%d %d", &n, &k);
    std::vector<std::tuple<long long, long long>> pan;
    for (int i = 0; i < n; ++i) {
      long long r,h;
      scanf("%lld %lld", &r, &h);
      pan.push_back(std::make_tuple(r, h));
    }

    std::sort(pan.rbegin(), pan.rend());
    long long whole = 0;
    for (std::size_t i = 0; i < pan.size(); ++i) {
      if (i == 0) {
        whole += (std::get<0>(pan[i]) * std::get<0>(pan[i]));
      }
      whole += (2 * std::get<0>(pan[i]) * std::get<1>(pan[i]));
    }

    for (int i = 0; i < n - k; ++i) {
      std::size_t pos = 0;
      long long minCur = 1000000000000000000;
      for (std::size_t i = 0; i < pan.size(); ++i) {
        long long all = 0;
        if (i == 0) {
          all += ((std::get<0>(pan[0]) * std::get<0>(pan[0]) - std::get<0>(pan[1]) * std::get<0>(pan[1])));
        }
        all += (2 * std::get<0>(pan[i]) * std::get<1>(pan[i]));

        if (minCur > all) {
          minCur = all;
          pos = i;
        }
      }
      
      whole -= minCur;
      pan.erase(pan.begin() + pos);
    }

    printf("Case #%d: %0.9Lf\n", test, static_cast<long double>(whole) * PI);
  }

  return 0;
}