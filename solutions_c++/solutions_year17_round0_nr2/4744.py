#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <string>
#include <queue>
#include <unordered_map>
using namespace std;

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int t; cin >> t;

  for (int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    string s; cin >> s;
    vector <int> v;

    for (int j = 0; j < s.length(); j++) {
      v.push_back(s[j] - '0');
      bool flag = false;
      for (int k = v.size() - 1; k - 1 >= 0; k--) {
        if (v[k - 1] > v[k]) {
          flag = true;
          v[k] = 9;
          v[k - 1]--;
        }
      }
      if (flag) {
        for (j = j + 1; j < s.length(); j++) {
          v.push_back(9);
        }
        break;
      }
    }
    int offset = 0;
    while (offset < v.size() && v[offset] <= 0) offset++;
    for (int i = offset; i < v.size(); i++) cout << v[i];
    cout << "\n";
  }

  return 0;
}
