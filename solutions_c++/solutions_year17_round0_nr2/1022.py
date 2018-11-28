#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

template<typename T> T next() { T tmp; cin >> tmp; return tmp; }


void solve() {
  string s = next<string>();
  for (int i = 0; i < s.size(); ++i) {
    string q = s;
    for (int j = i; j < q.size(); ++j) {
      q[j] = q[i];
    }
    if (q > s) {
      q[i] -= 1;
      for (int j = i + 1; j < q.size(); ++j) {
        q[j] = '9';
      }
      s = q;
      break;
    }
  }
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] != '0') {
      cout << s.substr(i) << endl;
      return;
    }
  }
}

int main() {
  int n = next<int>();
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  } 
  return 0;
}
