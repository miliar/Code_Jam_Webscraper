#include <bits/stdc++.h>

using namespace std;

int main () {
  long long n;
  int t, i, nines, c = 1;
  char s[20];
  
  cin >> t;
  while (t--) {
    cin >> n;
    for (i = 0; n; i++) {
      s[i] = '0' + n % 10;
      n = n / 10;
    }
    s[i] = 0;
    
    nines = -1;
    for (i = 0; s[i + 1]; i++) {
      if (s[i] < s[i + 1]) {
        s[i + 1]--;
        nines = i;
      }
    }
    if (s[i] == '0')
      i--;
    
    cout << "Case #" << c++ << ": ";
    while (i >= 0 && i > nines)
      cout << s[i--];
    while (nines-- >= 0)
      cout << "9";
    cout << endl;
  }
  return 0;
}

