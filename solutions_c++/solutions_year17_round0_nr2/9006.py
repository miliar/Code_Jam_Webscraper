#include <iostream>
#include <cstdint>


uint64_t tidy_it(uint64_t num) {
  unsigned cur, last;
  uint64_t mod = 10e18;
  uint64_t res = num;
  uint64_t aux = num;

  // Get power of 10 that represents largest digit
  while (mod > num)
    mod /= 10;

  cur = last = aux / mod;

  // 
  while (mod >= 1) {
    cur = aux / mod;

    if (last > cur)
      res = tidy_it(num - (num % mod + 1));

    aux -= mod * cur;
    mod /= 10;
    last = cur;
  }

  return res;
}

int main(int argc, char const *argv[]) {
  unsigned t;

  std::cin >> t;
  for (unsigned i = 1; i <= t; ++i) {
    uint64_t n, res;

    std::cin >> n;
    res = tidy_it(n);

    std::cout << "Case #" << i << ": " << res << std::endl;
  }

  return 0;
}
