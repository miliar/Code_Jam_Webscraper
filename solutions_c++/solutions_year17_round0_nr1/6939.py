#include <iostream>

using namespace std;

bool solved(const string &s) {
  int len = s.size();
  for(int i = 0; i < len; i++) {
    if(s[i] == '-') return false;
  }
  return true;
}

void flop(string &s, int x, int k) {
  for(int i = x; i < x + k; i ++) {
    if(s[i] == '-') {
      s[i] = '+';
    } else {
      s[i] = '-';
    }
  }
}

int main() {
  int T;
  cin >> T;
  int t = 1;
  while(t <= T) {
    string s;
    int k, len;
    cin >> s >> k;
    len = s.size();
    int ans = 0;
    for(int i = 0; i < len - k + 1; i ++) {
      if(s[i] == '-') {
	flop(s, i, k);
	ans ++;
      }
      //cout << s << endl;
    }
    if(solved(s)) {
      cout << "Case #" << t << ": " << ans << endl;
    } else {
      cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
    t ++;
  }
}
