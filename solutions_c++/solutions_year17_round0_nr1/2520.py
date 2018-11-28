#include <bits/stdc++.h>
#define el '\n'
using namespace std;

int k, ans;
string s;
bitset<1123> bb;

void solve(){
  ans = 0;
  for (int i = 0; i < s.size(); i++) bb[i] = (s[i] == '+' ? 1 : 0);
  ans = 0;
  for (int i = 0; i <= s.size()-k; i++){
    if (bb[i] == 0){
      for (int j = 0; j < k; j++) bb.flip(i+j);
      ans++;
    }
  }
  for (int i = 0; i < s.size(); i++) if (bb[i] == 0) ans = -1;
}

int main() 
{
  ios_base::sync_with_stdio(0); cin.tie(0);
    
  int t;
  cin >> t;
    
  for (int test = 1; test <= t; test++){
    cin >> s >> k;
    solve();
    if (ans == -1) cout << "Case #" << test << ": IMPOSSIBLE" << el;
    else cout << "Case #" << test << ": " << ans << el;
  }
    
  return 0;
}
