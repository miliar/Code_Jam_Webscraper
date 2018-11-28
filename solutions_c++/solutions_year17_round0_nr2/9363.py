// https://code.google.com/codejam/contest/3264486/dashboard#s=p1
#include <iostream>
using namespace std;

uint64_t pow_of_10[] = {
1,
10,
100,
1000,
10000,
100000,
1000000,
10000000,
100000000,
1000000000,
10000000000,
100000000000,
1000000000000,
10000000000000,
100000000000000,
1000000000000000,
10000000000000000,
100000000000000000,
1000000000000000000
};

bool isTidy(uint64_t num, int& violation) {
  int max_digit = 10;
  int pos = 0;
  while (num) {
    int last_digit = num % 10;
    if (last_digit > max_digit) {
      violation = pos;
      return false;
    }
    if (last_digit < max_digit)
      max_digit = last_digit;
    num = num / 10;
    pos++;
  }
  return true;
}

uint64_t getMaxTidy(uint64_t num) {
 
  int violation = 0;
  while (num && !isTidy(num, violation)) {
    // brute force approach
    //num--;
    num = (num - (num % pow_of_10[violation])) - 1;
  }
  return num;
}

int main() {
  int tests;
  cin >> tests;
  for (int i=0; i < tests; i++) {
    uint64_t num;
    cin >> num;
    cout << "Case #" << (i+1) << ": " << getMaxTidy(num) << endl;
  }
  return 0;
}
