#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <array>
#include <climits>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cstring>
#include <stack>
#include <queue>

using namespace std;


int main() {
  int t;
  cin >> t;

  queue<bool> cakes;
  for (int i_test = 0; i_test < t; ++i_test) {
    //char ch;
    //while (cin >> ch && ch != ' ') {
    //  if (ch == '+') {
    //    cakes.push(true);
    //  } else {
    //    cakes.push(false);
    //  }
    //}

    string str;
    cin >> str;

    int k;
    cin >> k;

    vector<bool> cakes(str.size());
    for (int i = 0; i < str.size(); ++i) {
      if (str[i] == '+') {
        cakes[i] = true;
      } else {
        cakes[i] = false;
      }
    }

    int count = 0;
    bool valid = true;
    for (int i = 0; i < cakes.size(); ++i) {
      if (!cakes[i]) {
        if (cakes.size() - i < k) {
          valid = false;
          break;
        } else {
          for (int j = i; j < i + k; ++j) cakes[j] = !cakes[j];
          ++count;
        }
      }
    }

    cout << "Case #" << i_test + 1 << ": ";
    if (valid) {
      cout << count;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }

  return 0;
}
