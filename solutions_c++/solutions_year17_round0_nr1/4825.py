
#include <iostream>
#include <string>

using namespace std;

void solve(){
  int ans = 0;
  string s;
  size_t k;
  cin >> s >> k;
  for(size_t i = 0; i < s.size()-k+1; ++i){
    if (s[i] == '-'){
      ++ans;
      for(size_t j = 0; j < k; ++j){
        char *c = &s[i+j];
        if(*c == '-') *c = '+';
        else *c = '-';
      }
    }
  }
  for (size_t i = s.size() - k + 1; i < s.size(); ++i){
    if(s[i] == '-'){
      cout << "IMPOSSIBLE" << endl;
      return;
    }
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
