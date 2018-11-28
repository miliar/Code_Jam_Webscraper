#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long li;

vector<li> tidy;

void brute(int length, int start, li cur) {
  if (length == 0) {
    tidy.push_back(cur);
    return;
  }

  for (int digit = start; digit <= 9; ++digit) {
    li next = cur * 10 + digit;
    brute(length - 1, digit, next);
  }
}

int main() {
  for (int ln = 1; ln <= 19; ++ln) {
    brute(ln, 1, 0);
    cerr << tidy.size() << endl;
  }

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    li n;
    cin >> n;

    auto upper = upper_bound(tidy.begin(), tidy.end(), n);
    assert(upper != tidy.begin());
    cout << *(--upper) << endl;
  }
  return 0;
}