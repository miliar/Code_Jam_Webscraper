#include <algorithm>
#include <cassert>
#include <iostream>
#include <iterator>
#include <map>

void flip(std::string& p, size_t idx, size_t K) {
  for (size_t i = idx; i < idx + K; ++i) {
    (&p[0])[i] = p.data()[i] == '-' ? '+' : '-';
  }
}

void solve(std::string S, uint64_t K, size_t testcase) {
  auto N = S.size();
  size_t nFlips = 0;
  size_t nFlipsB = 0;
  auto SF = S;
  for (size_t i = 0; i < N - K + 1; ++i) {
    if (SF[i] == '-') {
      flip(SF, i, K);
      nFlips++;
    }
  }

  auto SB = S;
  for (ssize_t i = N - 1; i >= K - 1; --i) {
    if (SB[i] == '-') {
      flip(SB, i - K + 1, K);
      nFlipsB++;
    }
  }

  for (size_t i = 0; i < N; ++i) {
    if (SF[i] == '-') {
      std::cout << "Case #" << testcase << ": "
                << "IMPOSSIBLE"
                << "\n";
      return;
    }
  }

  assert(nFlipsB == nFlips);

  std::cout << "Case #" << testcase << ": " << nFlips << "\n";
}

int main() {
  std::cout.setf(std::ios::unitbuf);  // unbuffered output

  uint64_t numberOfTestcases;
  std::cin >> numberOfTestcases;
  for (size_t i = 1; i <= numberOfTestcases; ++i) {
    std::string S;
    size_t K;
    std::cin >> S >> K;
    solve(S, K, i);
  }
  return 0;
}
