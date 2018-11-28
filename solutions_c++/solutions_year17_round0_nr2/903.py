#include <bits/stdc++.h>
using namespace std;

string solve(string n) {
  int flex = 0;
  int len = n.size();
  /*
     find this slope down
            v
     --------\
  */
  for (;flex < len - 1; flex++) {
    if (flex + 1 < len && n[flex] > n[flex+1]) {
      break;
    }
  }
  /*
     nothing need to be flexed
  */
  if (flex == len - 1) {
    return n;
  }
  /*
     find this (slope up)
      v
     /----------\
  */
  for (; flex > 0; flex--) {
    if (flex - 1 >= 0 && n[flex] > n[flex-1]) {
      break;
    }
  }
  n[flex]--;
  for (int i = flex+1; i < len; i++) {
    n[i] = '9';
  }
  if (n[0] == '0') {
    n.erase(0, 1);
  }
  return n;
}

int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    string n;
    cin >> n;
    cout << "Case #" << tc << ": " << solve(n) << endl;
  }
}
