#include<bits/stdc++.h>

using namespace std;

bool same[100005];

void solve(){
  string s; cin >> s;
  s = "+" + s;
  s = s + "+";
  int k; cin >> k;
  int n = s.length();
  for(int i=1;i<n;i++){
    same[i] = (s[i] == s[i-1]);
  }
  int ans = 0;
  for(int i=1;i<n;i++){
    if(same[i]) continue;
    ans++;
    if(i + k >= n){
      cout << "IMPOSSIBLE\n";
      return;
    }
    same[i+k] = !same[i+k];
  }
  cout << ans << "\n";
  return;
}

int main(){
  int T; cin >> T;
  for(int i=0;i<T;i++){
    cout << "Case #" << i+1 <<": ";
    solve();
  }
}
