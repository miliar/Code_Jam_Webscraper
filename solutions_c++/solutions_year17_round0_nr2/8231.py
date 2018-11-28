#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

int T;
string S;
int can(string s, int st, int v) {
  for (int i = st; i < s.length(); i++) {
    int c = s[i] - '0';
    if (c > v) return 1;
    if (c < v) return 0;
  }
  return 1;
}
int main() {
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> S;

    cout << "Case #" << t << ": ";
    int first = 1;
    for (int i = 0; i < S.length(); i++) {
      int d = S[i] - '0';
      if (can(S, i + 1, d)) {
        cout << d; 
        first = 0;
      } else {
        if (d - 1 > 0 || !first) cout << (d - 1);
        for (int rem = i + 1; rem < S.length(); rem++) cout << "9";
        break;
      }
    }
    cout << endl;
  } 
	return 0;
}
