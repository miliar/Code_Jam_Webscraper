#include <iostream>
#include <stdexcept>
#include <cstdint>

struct Sol {
  std::int64_t min;
  std::int64_t max;

  void compute(std::int64_t N, std::int64_t K);
};

void Sol::compute(std::int64_t N, std::int64_t K) {
  bool N_is_even  = (N % 2 == 0);
  bool N_is_odd   = !N_is_even;

  if (N == 1) {
    min = 0;
    max = 0;
    return;
  }

  if (K == 1) {
    if (N_is_odd) {
      min = (N - 1) / 2;
      max = (N - 1) / 2;
    } else {
      max = N / 2;
      min = N / 2 - 1;
    }
    return;
  }

  std::int64_t R = K - 1;

  bool R_is_even = (R % 2 == 0);
  bool R_is_odd  = !R_is_even;

  if (N_is_odd && R_is_odd) {
    compute((N - 1) / 2, (R - 1) / 2 + 1);
    return;
  }

  if (N_is_odd && R_is_even) {
    compute((N - 1) / 2, R / 2);
    return;
  }

  if (N_is_even && R_is_odd) {
    compute(N / 2, (R - 1) / 2 + 1);
    return;
  }

  if (N_is_even && R_is_even) {
    compute(N / 2 - 1, R / 2);
    return;
  }
}

int main(int argc, char **argv) {
  int T = 0;

  std::cin >> T;

  for (int i = 0; i < T; ++i) {
    std::int64_t N;
    std::int64_t K;

    std::cin >> N >> K;

    Sol sol;

    sol.compute(N, K);

    std::cout << "Case #" << (i + 1) << ": " << sol.max << " " << sol.min << std::endl;
  }

  return 0;
}
