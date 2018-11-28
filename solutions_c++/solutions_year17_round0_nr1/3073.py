#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

void solve() {
  string s;
  int k;
  cin >> s >> k;
  int ans = 0;
  for(int i = 0; i + k - 1 < s.size(); ++i){
    if(s[i] != '-'){
      continue;
    }
    for(int j = 0; j < k; ++j){
      s[i + j] ^= '-' ^ '+';
    }
    ans += 1;
  }
  if(count(s.begin(), s.end(), '-')){
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  cout << ans << endl;
}

int main() {
  int tests;
  cin >> tests;
  for(int test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";
    solve();
  }
}
