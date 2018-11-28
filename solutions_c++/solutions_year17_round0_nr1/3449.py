/**
 * Google Code Jam 2017
 * Autor: Gerson Lazaro <GersonLazaro@GersonLazaro.com>
 * 2017
 */

#include <bits/stdc++.h>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  int T, j, l, acum;
  bool flag;
  cin >> T;
  string s;
  int k;
  for(int i = 1; i <= T; i++) {
    cin >> s >> k;
    acum = 0;
    flag = true;
    for(j = 0; j <= s.size() - k; j++) {
      if(s[j] == '-') {
        acum++;
        s[j] = '+';
        for(l = 1; l < k; l++) {
          if(s[j + l] == '-') s[j + l] = '+';
          else s[j + l] = '-';
        }
      }
    }
    for(j = s.size() - k + 1; j < s.size(); j++) {
      if(s[j] == '-') {
        flag = false;
        break;
      }
    }
    cout << "Case #" << i << ": ";
    if(flag) cout << acum << "\n";
    else cout << "IMPOSSIBLE\n"; 
    
  }
  return 0;
}