#include <iostream>
#include <algorithm>
#include <string>

uint64_t solve(uint64_t N)
{
  std::string S = std::to_string(N);

  for (long i = S.size() - 1; i > 0; --i) {
    if (S[i - 1] > S[i]) {
      --S[i - 1];
      for (unsigned j = i; j < S.size(); ++j) {
        S[j] = '9';
      }
    }
  }

  return std::stoull(S);
}

int main()
{
  unsigned T;
  std::cin >> T;

  for (unsigned t = 0; t < T; ++t) {
    uint64_t N;
    std::cin >> N;

    std::cout << "Case #" << (t + 1) << ": " << solve(N) << std::endl;
  }

  return 0;
}
