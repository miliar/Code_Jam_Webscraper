#include <bits/stdc++.h>

using namespace std;

int main () {
  int t, i, n, caso, resp, k, j;
  char s[1010];
  
  cin >> t;  
  for (caso = 1; caso <= t; caso++) {
    cin >> s >> k;
    n = strlen (s);
    resp = 0;
    for (i = 0; s[i]; i++) {
      if (s[i] == '-') {
        if (i + k <= n) {
          resp++;
          for (j = 0; j < k; j++) {
            if (s[i + j] == '+')
              s[i + j] = '-';
            else
              s[i + j] = '+';
          }
        }
        else {
          resp = -1;
          break;
        }
      }
    }
    
    cout << "Case #" << caso << ": ";
    if (resp == -1)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << resp << endl;
  }
  
  return 0;
}

