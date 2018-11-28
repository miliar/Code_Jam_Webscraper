#include <bits/stdc++.h>
using namespace std;

string solve(string s) {
  //cout << s << endl;
  long long ret = s[0] - '0';
  
  int i = 1;
  for (i = 1; i < s.length(); i++) {
    if (s[i-1] > s[i]) {
      break;
    } else {
      ret = ret * 10 + (s[i] - '0');
    }
  }

  if (i >= s.length()) {
    return s;
  } else {
    ret -= 1;
    string sret = "";
    while (ret) {
      sret = char(ret % 10 + '0') + sret;
      ret /= 10;
    }
    //cout << "  " << sret << endl;
    string front = solve(sret);
    string rem = "";
    for (; i < s.length(); i++) {
      rem += '9';
    }

    return front + rem;
  }
}

int T;
string s;

int main() {

  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> s;

    string ans = solve(s);

    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;
}