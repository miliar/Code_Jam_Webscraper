#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>

#define taskname "B-small-attempt3"

using namespace std;

void minus_one(string& s, int pos) {
//  cerr << s << endl;
  if (s[pos] != '0') {
    s[pos]--;
  } else {
    s[pos] = '9';
    minus_one(s, pos + 1);
  }
}

int main() {
	freopen(taskname".in", "r", stdin);
	freopen(taskname".out", "w", stdout);

  string s;
  int t;
  cin >> t;
  for (int h = 1; h <= t; h++) {
    cin >> s;
    reverse(s.begin(), s.end());

    while (s > "") {
      bool flag = true;
      for (int i = 0; i < s.size() - 1; i++) {
        if (s[i] < s[i + 1]) {
          flag = false;
          break;
        }
      }
      if (flag) {
        reverse(s.begin(), s.end());
        cout << "Case #" <<  h << ": " + s << endl; 
        break;
      }
      minus_one(s, 0);
      int cnt = 0;
      for (int i = s.size() - 1; i >= 0; i--) {
        if (s[i] != '0') {
          break;
        }
        cnt++;
      }

      s = s.substr(0, s.size() - cnt);
    }
  }
  return 0;
}
