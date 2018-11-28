#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <unordered_map>
#include <vector>


#define INF 1000000002486618624LL
#define MOD 1000000007
#define ALL(x) std::begin(x), std::end(x)
#define RALL(x) (x).rbegin(), (x).rend()


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  std::cout << std::fixed << std::setprecision(9);

  int T, N, K;

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> N >> K;

    std::vector<long double> R(N), H(N);

    for (int i = 0; i < N; i ++)
      std::cin >> R[i] >> H[i];

    double sp = 0.0;

    for (int i = 0; i < N; i ++) {
      long double s0 = R[i] * R[i] + 2.0 * R[i] * H[i];

      std::vector<std::pair<long double, int>> a;

      for (int j = 0; j < N; j ++)
        if (j != i)
          if (R[j] <= R[i])
            a.emplace_back(2.0 * R[j] * H[j], j);

      std::sort(RALL(a));

      if (a.size() > K - 1)
        a.resize(K - 1);

      long double s1 = 0.0;

      for (const auto& pair : a)
        s1 += pair.first;

      long double s = s0 + s1;

      if (s > sp)
        sp = s;
    }

    std::cout << "Case #" << t << ": " << sp * M_PI << std::endl;
  }
  
  return 0;
}
