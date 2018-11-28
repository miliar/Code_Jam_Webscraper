#include <iostream>

using namespace std;


void test() {
  string s;
  int k;
  cin >> s >> k;
  
  int ans = 0;
  
  for(int i = 0; i <= s.length() - k; i++) {
    if(s[i] == '-') {
      ans++;
      for(int j = i; j < i + k; j++) {
        s[j] = '+' + '-' - s[j];
      }
    }
  }
  
  bool ok = true;
  for(int i = s.length() - k; i < s.length(); i++) {
    if(s[i] == '-') {
      ok = false;
      break;
    }
  }
  
  if(ok) {
    cout << ans << '\n';
  } else {
    cout << "IMPOSSIBLE\n";
  }
}


int main() {
  int t;
  cin >> t;
  
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    test();
  } 
  
  return 0;
}
