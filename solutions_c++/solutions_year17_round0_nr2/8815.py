#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

uint64_t find_num (uint64_t num) {
  uint64_t digit,digit_prev,number;
  while (true) {
    number = num;
    //cout << "Number=" << number << endl;
    while (true) {
      digit = number%10;
      number = number/10;
      if (number==0) {
	return num;
      }
      digit_prev = number%10;
      //cout << "Digit=" << digit << " Digit_prev=" << digit_prev  << endl;
      if (digit_prev > digit)  {
        break;
      }
    }
    num--;
  } 
}

int main() {
  uint64_t t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    n = find_num(n);
    cout << "Case #" << i << ": " << n << endl;
  }
  return 0;
}
