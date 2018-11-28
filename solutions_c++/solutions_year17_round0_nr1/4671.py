#include <vector>
#include <iostream>
#include <string>

using namespace std;

void solve(int i) {
  cout << "Case #" << i+1 << ": ";
  string s;
  cin >> s;
  int l;
  cin >> l;
  int res = 0;
  for (int i=0; i<s.length(); i++) {
    if (s[i] == '-') {
      for (int j=0; j<l; j++) {
        if (s[i+j]=='-') s[i+j] = '+'; else s[i+j] = '-';
        if (i+j>=s.length()) {
          cout<< "IMPOSSIBLE" << endl;
          return;
        }
      }
      res++;
    }
  }
  cout << res << endl;
}

int main() {
  int T;
  cin >> T;
  for (int k=0; k<T; k++) {
    solve(k);
    
  }
  return 0;
}
