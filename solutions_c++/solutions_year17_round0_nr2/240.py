#define NDEBUG
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;


string solve() {
  string num;
  cin >> num;
  bool ok;
  do {
    ok = true;
    for (int i = (int)num.size() - 1; ok && i >= 0; --i) {
      for (int j = i + 1; ok && j < (int)num.size(); ++j) {
        if (num[i] > num[j]) {
          assert(num[i] > '0');
          --num[i];
          fill(num.begin() + i + 1, num.end(), '9');
          break;
        }
      }
    }
  } while (!ok) ;
  return num.substr(num.find_first_not_of("0"));
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": " << solve() << '\n';
  }
}
