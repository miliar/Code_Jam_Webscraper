#include <bits/stdc++.h>
using namespace std;

int main() {
  freopen("b1.in", "r", stdin);
  freopen("b1.out", "w", stdout);
  int kase;
  cin >> kase;
  for(int k = 0; k < kase; k++) {
    string s;
    cin >> s;
    int len = s.size();
    for(int i = len - 1; i > 0; i--) {
      if(s[i] < s[i - 1]) {
        for(int j = i; j < len; j++) {
          s[j] = '9';
        }
        s[i - 1]--;
      }
    }
    reverse(s.begin(), s.end());
    while(s[s.size() - 1] == '0') s.pop_back();
    reverse(s.begin(), s.end());
    cout << "Case #" << k + 1 << ": " <<  s << endl;
  }
  return 0;
}
