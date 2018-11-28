#include <iostream>

std::pair<int64_t, int64_t> play(int64_t N, int64_t K) {
  int64_t pow2 = 1;
  while (pow2 <= K) {
    pow2 *= 2;
  }
  pow2 /= 2;
  
  int64_t N_j = N / pow2;
  int64_t R_j = N - N_j * pow2;
  
  // We have (R_j+1) blocks of N_j
  //     and (pow2 - (R_j+1)) blocks of N_j - 1
  
  int64_t K_j = K - (pow2 - 1);
  if (K_j <= (R_j + 1)) {
    return std::make_pair((N_j / 2), (N_j - 1) / 2);
  } else {
    return std::make_pair((N_j - 1) / 2, ((N_j - 1) - 1) / 2);
  }
}

int main() {
  int64_t nTests;
  int64_t N, K;
  
  std::cin >> nTests;
  for (size_t i = 0; i < nTests; ++i) {
    std::cin >> N >> K;
    auto x = play(N, K);
    std::cout << "Case #" << (i+1) << ": " << x.first << " " << x.second << std::endl;
  }
}
