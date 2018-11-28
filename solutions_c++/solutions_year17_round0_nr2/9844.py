#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

bool is_tidy(long n) {
  int last = 10;
  int curr;
  while (n > 0) {
    curr = n % 10;
    if (last < curr) {
      return false;
    } else {
      last = curr;
      n /= 10;
    }
  }
  return true;
}

int main() {
  long t;
  cin >> t;
  for (long i = 1; i <= t; ++i) {
    long n;
    cin >> n;
    
    while (!is_tidy(n)) {
      n -= 1;
    }

    cout
      << "Case #" << i << ": "
      << n
      << endl;
  }
}
