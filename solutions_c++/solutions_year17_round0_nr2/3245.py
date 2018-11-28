#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

void decrease(string& origin, int pos) {
  // from 0 to pos are non decreasing
  if (pos == 0) {
    origin[pos] -= 1;
    if (origin[pos] == '0') {
      origin.erase(0,1);
    }
  }
  else {
    if (origin[pos] > origin[pos-1]) {
      origin[pos] -= 1;
    }
    else {
      // origin[pos] == origin[pos-1]
      origin[pos] = '9';
      decrease(origin, pos-1);
    }
  }
}
void tidy(string& input) {
  char prev = input[0];
  // find first decreasing
  int dec = 0;
  for (++dec; dec < (int)input.size(); ++dec) {
    if (input[dec] >= prev) {
      prev = input[dec];
    }
    else {
      break;
    }
  }
  if (dec == (int)input.size()) {
    return;
  }
  // need to find last tidy number
  for (int change = dec; change < (int)input.size(); ++change) {
    input[change] = '9';
  }
  --dec;
  decrease(input, dec);
}

int main() {
  int t;
  string number;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  cin.ignore();
  string cake;
  for (int i = 1; i <= t; ++i) {
    getline(cin, number);
    tidy(number);
    cout << "Case #" << i << ": " << number << endl;
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    // out put
    // Case #x: y
  }
}