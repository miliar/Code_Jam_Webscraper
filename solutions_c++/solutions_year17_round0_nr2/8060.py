#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdint>

int main()
{
  int T;
  std::cin >> T;
  for (int i = 0; i < T; i++) {
    uint64_t N;
    std::cin >> N;
    bool fin = true;
    while (fin) {
      uint64_t Np = N;
      fin = false;
      for (uint64_t j = 10; j <= N; j *=10 ) {
        const uint64_t l = (N % j) / (j / 10);
        const uint64_t ll = j == 10 ? (N % j) : (N % (j/ 10));
        const uint64_t h = (N % (j * 10)) / j;
        if (l < h) {
          if (Np == N) {
            Np -= ll + 1;
          }
          N = Np;
          fin = true;
          break;
        } else if (l == 0 && h == 0 && Np == N) {
          Np -= (l + 1) * (j / 10);          
        }
      }
    }
    std::cout << "Case #" << i + 1 << ": ";
    std::cout << N << std::endl;
  }
  return 0;
}
