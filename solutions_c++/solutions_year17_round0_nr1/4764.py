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

  for (int testCase = 1; testCase <= t; testCase++) {
    cout << "Case #" << testCase << ": ";
    string s; cin >> s;
    int k; cin >> k;
    int res = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
      if (s[i] == '-' && i < k - 1) {
        res = -1;
        break;
      } else if (s[i] == '-') {
        res++;
        for (int j = i - k + 1; j <= i; j++) {
          s[j] = s[j] == '+' ? '-' : '+';
        }
      }
    }
    if (res == -1) cout << "IMPOSSIBLE\n";
    else cout << res << "\n";
  }

  return 0;
}
