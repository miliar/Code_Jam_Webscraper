#include <iostream>
#include <cstring>

using namespace std;

const int N = 1000;

char s[N+1];

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    cin >> s;
    int k; cin >> k;
    int n = strlen(s);
    for (int i = 0; i < n; i++) s[i] = (s[i] == '+' ? 0 : 1);
    int res = 0;
    for (int i = 0; i < n; i++) {
      if (s[i]) {
        if (i+k <= n) {
          res++;
          for (int j = 0; j < k; j++) s[i+j] ^= 1;
        } else {
          res = -1;
          break;
        }
      }
    }
    if (res < 0)
      cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << tt << ": " << res << endl;
  }
  return 0;
}

