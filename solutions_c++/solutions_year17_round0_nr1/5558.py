#include <sstream>
#include <cassert>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <list>
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long tint;
typedef unsigned int uint;
const int MAXN = 1073741824;
const int MAX_INT = 2147483647;

int main() {
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    string s;
    cin >> s;
    int k;
    cin >> k;
    int count = 0;
    int n = s.size();
    int check = 0;
    for (int i = 0; i + k <= n; i++) {
      check++;
      if (s[i] == '-') {
        count++;
        for (int j = i; j < i + k; j++) {
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        }
      }
    }
    for (int i = n - k + 1; i < n; i++) {
      check++;
      if (s[i] == '-') count = -1;
    }
    assert(check == n);
    cout << "Case #" << tt << ": ";
    if (count < 0) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << count << endl;
    }
  }

  return 0;
}
