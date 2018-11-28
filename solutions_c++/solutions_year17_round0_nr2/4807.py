
#include <iostream>
#include <string>

using namespace std;

void solve(){
  string ans;
  string s;
  cin >> s;
  char m = 0;
  size_t pos = 0;
  for(size_t i = 0; i <= s.size(); ++i){
    if(i == s.size()){
      pos = i;
      break;
    }
    if(s[i] < m) break;
    if(s[i] > m) pos = i;
    m = s[i];
  }
  for(size_t i = 0; i < pos && i < s.size(); ++i){
    ans.push_back(s[i]);
  }
  if(pos < s.size() && s[pos] != '1') ans.push_back(s[pos]-1);
  for(size_t i = pos+1; i < s.size(); ++i){
    ans.push_back('9');
  }
  cout << ans << endl;
  return;
}

int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; ++i){
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
