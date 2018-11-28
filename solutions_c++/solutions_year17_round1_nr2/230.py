#include <algorithm>
#include <iostream>
#include <string>
#include <vector>


namespace {

int Solve(std::vector<int> R, std::vector<std::vector<int>> Q) {
  const int N = Q.size();
  const int P = Q[0].size();
  for (auto& packages : Q) std::sort(packages.begin(), packages.end());
  std::vector<std::vector<int>> min_servings(N);
  std::vector<std::vector<int>> max_servings(N);
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < P; ++j) {
      int min = Q[i][j] * 10 / (R[i] * 11);
      min += min * R[i] * 11 < Q[i][j] * 10;
      int max = Q[i][j] * 10 / (R[i] * 9);
      if (min <= max) {
        min_servings[i].push_back(min);
        max_servings[i].push_back(max);
      }
    }
  }

  std::vector<int> used(N);
  int result = 0;
  while (true) {
    int lower = 0;
    for (int i = 0; i < N; ++i) {
      if (used[i] == min_servings[i].size()) return result;
      lower = std::max(lower, min_servings[i][used[i]]);
    }
    bool possible = true;
    for (int i = 0; i < N; ++i) {
      if (max_servings[i][used[i]] < lower) {
        possible = false;
        break;
      }
    }
    if (possible) {
      ++result;
      for (int& count : used) ++count;
    } else {
      for (int i = 0; i < N; ++i) {
        if (max_servings[i][used[i]] < lower) {
          ++used[i];
        }
      }
    }
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
    std::vector<int> R(N);
    for (int j = 0; j < N; ++j) {
      std::cin >> R[j];
    }
    std::vector<std::vector<int>> Q(N, std::vector<int>(P));
    for (int j = 0; j < N; ++j) {
      for (int k = 0; k < P; ++k) {
        std::cin >> Q[j][k];
      }
    }
    std::cout << "Case #" << i << ": " << Solve(R, Q) << std::endl;
  }

  return 0;
}
