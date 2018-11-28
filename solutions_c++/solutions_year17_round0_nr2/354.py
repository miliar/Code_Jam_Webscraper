#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
    string n;
    cin >> n;

    string s = n;
    for (int i=n.length()-2;i>=0;i--) {
      s[i] = min(s[i], s[i+1]);
    }

    string ans = n;
    for (int i=0;i<n.length();i++) {
      if (n[i] <= s[i]) {
        continue;
      }
      else {
        int j=i+1;
        if (i+1 < n.length() && n[i+1] > n[i]) {
          ans[i+1]--;
          j++;
        }
        else {
          ans[i] = n[i]-1;
        }
        for (;j<n.length();j++) ans[j] = '9';
        break;
      }
    }
    while (ans[0] == '0') {
      ans = ans.substr(1);
    }
    //printf("Case #%d: %s -> %s\n", t, n.c_str(), ans.c_str());
    printf("Case #%d: %s\n", t, ans.c_str());
  }

}
