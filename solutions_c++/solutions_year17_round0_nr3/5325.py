#include <iostream>

using i64 = unsigned long long int;

void solve(i64 N, i64 K);

int main(int argc, char **argv) {
  int T;
  std::cin >> T;

  for (int x = 1; x <= T; ++x) {
    i64 N, K;
    std::cin >> N >> K;
    std::cout << "Case #" << x << ": ";
    solve(N, K);
    std::cout << std::endl;
  }

  //i64 N, K;
  //std::cin >> N >> K;
  //solve(N, K);
  //std::cout << std::endl;

  return 0;
}

void solve(i64 N, i64 K) {
  while (K > 1) {
    if (N % 2 == 0 && K % 2 != 0) {
      --N;
    }
    N /= 2;
    K /= 2;
  }

  i64 x = N / 2;
  if (N % 2 == 0) {
    std::cout << x << " " << x-1;
  } else {
    std::cout << x << " " << x;
  }
}
