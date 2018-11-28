#include <cmath>
#include <iostream>

bool check_number(long n)
{
  // Note that digits are traversed from last to first
  long next_digit = n % 10;
  n = n / 10;
  while (n) {
    long digit = n % 10;
    if (digit > next_digit)
      return false;
    next_digit = digit;
    n = n / 10;
  }

  return true;
}

int main(int argc, char* argv[])
{
  unsigned T;
  long N;
  long n;
  std::cin >> T;
  for (auto t = 1; t <= T; ++t) {
    std::cin >> N;
    for (n = N; n > 0; --n) {
      if (check_number(n)) {
        std::cout << "Case #" << t << ": " << n << std::endl;
        break;
      }
    }
  }
  return 0;
}
