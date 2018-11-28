#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

uint64_t checkDigits(const uint64_t inumber) {
  uint64_t number = inumber;
  //  cout << "IN: " << number << endl;
  int last = -1;
  int count = 0;
  while (number > 0) {
    int i = number % 10;
    // cout << "N: " << number << endl;
    if (last < 0 || last >= i) {
      last = i;
    } else {
      number *= pow(10, count);
      int64_t decrease = inumber - number;
      // cout << "C: " << count << "CN: " << number << " D: " << decrease << endl;

      if (decrease <= 1) {
        return 1;
      } else {
        return decrease;
      }
    }

    number /= 10;
    ++count;
  }

  return 0;
}

int main() {
  uint64_t t, n;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n;
    for (uint64_t value = n; value > 0;) {
      // cout << "V: " << value << endl;
      uint64_t c = checkDigits(value);
      // cout << "C: " << c << endl;
      if (c == 0) {
	       cout << "Case #" << i << ": " << value << " " << endl;
	       break;
      } else {
        value -= c;
      }
    }
  }
  return 0;
}
