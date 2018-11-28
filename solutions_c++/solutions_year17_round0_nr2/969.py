#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {

    int ret = 0;
    string s;
    cin >> s;
    for(int i=s.size()-2;i>=0;i--) {
      if(s[i] <= s[i+1]) continue;
      else {
        s[i] --;
        for(int j=i+1;j<s.size();j++) s[j] = '9';
      }
    }
    while(s[0] == '0' && s.size() > 1) {
      s = s.substr(1, s.size()-1);
    }
    printf("Case #%d: ",tc);
    cout << s << endl;
  }

  return 0;
}