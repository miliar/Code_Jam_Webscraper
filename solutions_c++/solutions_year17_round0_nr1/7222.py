#include <iostream>
#include <string>

using namespace std;

int op(char c) {
  return (c == '-')?'+':'-';
}

int main() {
  int T;
  cin>>T;
  for (int k = 0; k < T; k++) {
    string s;
    int x;
    cin>>s>>x;
    int ans = 0;
    int sz = s.size();
    for (int i = 0; i < sz; i++) {
      if (s[i] == '-') {
        if (sz - i >= x) {
          ans++;
          for (int j = i; j < i + x; j++)
            s[j] = op(s[j]);
        } else {
          ans = -1;
          break;
        }
      }
    }

    cout<<"Case #"<<(k+1)<<": ";
    if (ans >= 0) {
      cout<<ans<<endl;
    } else {
      cout<<"IMPOSSIBLE"<<endl;
    }
  }
}
