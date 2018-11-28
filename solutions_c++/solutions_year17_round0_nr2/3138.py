#include <iostream>
#include <cstdint>

using namespace std;

uint64_t get_last_tidy(uint64_t n) {
  uint64_t divisor = 1;
  uint64_t next_divisor = 10;
  // Find the first divisor
  while((n / next_divisor) != 0) { 
    uint64_t digit = (n / divisor) % 10;
    uint64_t next_digit = (n / next_divisor) % 10;
    if (digit < next_digit) {
      n = ((n / next_divisor) * next_divisor) - 1;
    }
    divisor = next_divisor;
    next_divisor *= 10;
  }
  return n;
}

int main(int argc, char **argv) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    uint64_t n;
    cin >> n;
    cout << "Case #" << i + 1 << ": " << get_last_tidy(n) << endl;
  }
  return 0;
}