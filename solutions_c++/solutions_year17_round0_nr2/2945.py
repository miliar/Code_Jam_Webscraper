#include <iostream>
using namespace std;

string s;

string solve() {
  cin >> s;

  for(int i = 1; i < s.size(); i++) {
    if(s[i] < s[i-1]) {

      char o = s[i-1];
      int j;
      for(j = i-1; j>=0 && s[j] == o; j--) {
        s[j]--;
      }

      if(j != i-2) {
        fill(s.begin() + j + 2, s.begin() + i, '9');
      }

      if(o == '1') {
        s = string(s.size() - 1, '9');
      } else {
        fill(s.begin() + i, s.end(), '9');
      }
    }
  }

  // single digits
  return s;
}

int main () {
  int t;

  cin >> t;
  for(int i = 1; i <= t; i++)
  {
    printf("Case #%d: %s\n", i, solve().c_str());
  }

  return 0;
}
