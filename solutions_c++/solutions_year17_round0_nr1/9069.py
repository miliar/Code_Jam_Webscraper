#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, num, flip, cakes, flipCount;
  string str;
  bool success;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

  for (int i = 1; i <= t; ++i) {
    cin >> str >> flip;
    success = true;
    flipCount = 0;
    num = str.length();
    for (int j = 0; j <= num - flip; j++) {
      if (str.at(j) == '+') {
      	continue;
      }
      flipCount ++;
      for (int k = 0; k < flip; k++) {
      	if (str.at(j+k) == '+') {
      	  str.at(j+k) = '-';
      	} else {
          str.at(j+k) = '+';
      	}
      }
    }
    for (int j = 1; j <= flip; j++) {
      if (str.at(str.length() - j) == '-') {
        success = false;
      }
    }
    if (success) {
      cout << "Case #" << i << ": " << flipCount << endl;
    } else {
      cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}