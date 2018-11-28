#include <iostream>
using namespace std;
int main() {
  int t;
  string n, ans;
  int l, c, f; // last digit, current digit, first drop

  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> n;
    ans = n;
    l = 0;
    f = n.size();
    for(int j = 0; j < n.size(); j++) {
      c = n[j]-'0';
      if(c < l) {
        f = j;
        break;
      }
      l = c;
    }
    for(int j = f; j < n.size(); j++) {
      ans[j] = '9';
    }
    if(f != n.size())
    for(int z = f-1; z>=0; z--) {
      ans[z]-=1; // if ans[q] == 0 <=> n == 0
      // devo sistemare ans[0...z]
      if(z != 0 and ans[z] < ans[z-1]) {
        ans[z] = '9';
      }
      else {
        break;
      }
    }
    printf("Case #%d: ", i);
    for(int j = 0; j < ans.size(); j++) {
      if(ans[j] != '0' or j == ans.size()-1)
        cout << ans[j];
    }
    cout << '\n';
  }
}
