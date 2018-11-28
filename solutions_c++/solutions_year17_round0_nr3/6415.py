#include <iostream>
#include <vector>
#include <tuple>

std::tuple<long, long> solve(long n, long k);
std::tuple<long, long> solve(long n, long k) {
  long bigCount = 1;
  long smallCount = 0;

  while(n > 0) {
    // Allocate big first, due to maxarg (max(l, r)) constraint
    k -= bigCount;
    if(k <= 0) break;
    long bigCountNext = (n % 2 == 0)
      ? bigCount      // if even, then each will be split into a big and a small one
      : 2* bigCount;  // if odd, then each will be split into two big ones

    n -= 1;
    k -= smallCount;
    bigCountNext += (n % 2 == 0)
      ? smallCount  // if even, then each will be split into a big and a small one
      : 0;          // if odd, each will be split into two small ones
    if(k <= 0) break;
    n += 1;
    n /= 2;
    smallCount = 2 * (bigCount + smallCount) - bigCountNext;
    if(n - 1 <= 0) smallCount = 0;
    bigCount = bigCountNext;
  }

  return std::make_tuple(n / 2, (n - 1) / 2);
}

int main() {
  int numCases;
  std::cin >> numCases;
  for(int i = 1; i <= numCases; ++i) {
    long n, k;
    std::cin >> n >> k;
    long max_val, min_val;
    std::tie(max_val, min_val) = solve(n, k);
    std::cout << "Case #" << i << ": " << max_val << " " << min_val << std::endl;
  }
}
