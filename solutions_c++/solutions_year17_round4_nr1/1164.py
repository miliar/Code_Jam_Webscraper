#include <cassert>

#include <algorithm>
#include <iostream>
#include <vector>


namespace {

int Solve(int P, std::vector<int> G) {
  std::vector<int> counts(P);
  for (int g : G) ++counts[g % P];
  int result = counts[0];
  if (P == 2) {
    result += (counts[1] + 1) / 2;
  } else if (P == 3) {
    const int a = std::min(counts[1], counts[2]);
    result += a;
    for (int i : {1, 2}) result += (counts[i] - a + 2) / 3;
  } else if (P == 4) {
    {
      const int a = std::min(counts[1], counts[3]);
      result += a;
      for (int i : {1, 3}) counts[i] -= a;
    }
    {
      result += counts[2] / 2;
      counts[2] -= counts[2] / 2 * 2;
    }
    {
      int a = counts[1] + counts[3];
      int b = counts[2];
      if (a >= 2 && b == 1) {
        ++result;
        a -= 2;
        --b;
      }
      {
        result += a / 4;
        a -= a / 4 * 4;
      }
      if (a + b > 0) ++result;
    }
  } else {
    assert(false);
  }
  return result;
}

}  // namespace


int main(void) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, P;
    std::cin >> N >> P;
    std::vector<int> G(N);
    for (int j = 0; j < N; ++j) {
      std::cin >> G[j];
    }
    std::cout << "Case #" << i << ": " << Solve(P, G) << std::endl;
  }

  return 0;
}
