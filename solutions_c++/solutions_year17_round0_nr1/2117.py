#include <iostream>
#include <string>


namespace {

std::string Solve(std::string S, int K) {
  const int N = S.size();
  int count = 0;
  for (int right = K; right <= N; ++right) {
    const int left = right - K;
    if (S[left] == '-') {
      ++count;
      for (int i = left; i < right; ++i) {
        S[i] = (S[i] == '-') ? '+' : '-';
      }
    }
  }
  if (S.substr(N - K) != std::string(K, '+')) {
    return "IMPOSSIBLE";
  }
  return std::to_string(count);
}

}  // namespace


int main(void) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    std::string S;
    int K;
    std::cin >> S >> K;
    std::cout << "Case #" << i << ": " << Solve(S, K) << std::endl;
  }

  return 0;
}
