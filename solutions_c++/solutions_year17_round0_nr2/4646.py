#include <vector>
#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

using namespace std;

void solve(int i) {
  cout << "Case #" << i+1 << ": ";
  string s;
  cin >> s;
  char status;
  if (s.length()==1)
    cout << s << endl;
  else {
    int flag = 0;
    bool fallen = false;
    string res;
    res += s[0];
    for (int i=1; i<s.length(); i++) {
      if (fallen) {
        res += '9';
        continue;
      }
      if (s[i]<s[i-1]) {
        for (int j=i-1; j>flag; j--)
          res[j] = '9';
        res[flag]--;
        fallen = true;
        res += '9';
      } else res += s[i];
      if (s[i] != s[i-1]) flag = i;
    }
    cout << atoll(res.c_str()) << endl;
  }
}

int main() {
  int T;
  cin >> T;
  for (int k=0; k<T; k++) {
    solve(k);
  }
  return 0;
}
