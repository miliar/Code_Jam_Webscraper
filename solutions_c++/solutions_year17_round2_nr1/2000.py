#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <fstream>
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


int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  std::cout << std::fixed << std::setprecision(9);

  int Q, D, N;

  std::cin >> Q;

  for (int q = 1; q <= Q; q ++) {
    std::cin >> D >> N;

    std::vector<int> K(N), S(N);

    double tp = -1e+9;

    for (int i = 0; i < N; i ++) {
      std::cin >> K[i] >> S[i];

      tp = std::max(1. * (D - K[i]) / S[i], tp);
    }

    double s = D / tp;

    std::cout << "Case #" << q << ": " << s << std::endl;
  }

  return 0;
}
