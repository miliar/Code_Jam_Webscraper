//
// Created by Michael on 4/8/2017.
//

#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>

using namespace std;

long long findTidyNumber(long long number) {
  for (long long j = number; j > 1; --j) {
    std::string aNumber = to_string(j);
    bool smaller = true;
    for (int c = 0; c < aNumber.size() - 1; ++c) {
      if (aNumber.at(c) > aNumber[c + 1]) {
        smaller = false;
        break;
      }
    }
    if (smaller) {
      return j;
    }
  }
}

string efficientTidyNumber(long long number) {
  std::string aNumber = to_string(number);
  std::string result;
  for (auto c = aNumber.size() - 1; c > 0; --c) {
    for (auto d = 0; d < aNumber.size(); ++d) {
      if (aNumber.at(d) < aNumber.at(c)) {
        aNumber[c] = '9';
        aNumber.at(aNumber.size() - c) -= 1;
        break;
      }
    }
  }
  return aNumber;
}

int main() {
  int cases = 0;
  cin >> cases;
  for (int i = 0; i < cases; ++i) {
    long long number;
    cin >> number;
    long long foundNum = findTidyNumber(number);
    //string foundNum = efficientTidyNumber(number);
    cout << "Case #" << i + 1 << ": " << foundNum << endl;
  }
}