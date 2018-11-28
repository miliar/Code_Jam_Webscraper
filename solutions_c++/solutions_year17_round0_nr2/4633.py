#include <iostream>

using namespace std;


void solve() {
  string s;
  cin >> s;
  int i = s.size() - 1;
  int nines = 0;
  while(i > 0) {
    if(s[i] < s[i-1]){
      s[i-1]--;
      nines = s.size() - i;
    }
    i--;
  }
  bool flag = true;
  for(int i = 0;i<s.size() - nines;i++) {
    if(flag && s[i] == '0')
      continue;
    flag = true;
    cout << s[i];
  }
  for(int i =0;i<nines;i++)
    cout << 9;
}


int main() {
  int T;
  cin >> T;
  for(int t = 1; t<=T;t++) {
    cout << "Case #" << t << ": ";
    solve();
    cout << endl;
  }
}
