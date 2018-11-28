#include <iostream>
#include <vector>
#include <string>


int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) {
    long long n, k;
    std::cin >> n >> k;
    // find the largest m such that pow = 2^m <= k
    long long pow = 1LL;
    while (2*pow <= k)
      pow *= 2;
    long long small = (n-pow+1) / pow;
    long long nlarge = (n-pow+1) - small*pow;
    long long occupiedlarge = k - pow;
    long long kth = (occupiedlarge >= nlarge) ? small : small+1;

    std::cout << "Case #" << t+1 << ": " <<  kth/2 << " " << (kth-1)/2 << std::endl;
  }
  return EXIT_SUCCESS;
}
