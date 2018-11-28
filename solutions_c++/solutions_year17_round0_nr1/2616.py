#include <iostream>
using namespace std;
int main() {
  int t, k;
  string s;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> s >> k;
    int ans = 0;
    bool can = true;
    for(int j = 0; j < s.size(); j++) {
      if(s[j] == '-') {
        ans++;
        for(int q = 0; q < k; q++) {
          if(j+q >= s.size()) {
            can = false;
            break;
          }
          s[j+q] = s[j+q] == '-' ? '+' : '-';
        }
      }
    }
    if(can)
      printf("Case #%d: %d\n", i, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", i);
  }
}
