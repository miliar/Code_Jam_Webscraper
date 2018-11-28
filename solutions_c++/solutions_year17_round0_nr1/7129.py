#include <iostream>
#include <vector>
#include <string>

using namespace std;

extern int solve(string s, int K);

int main() {
  int T;
  cin >> T;
  cerr << "T: " << T << endl;
  
  for (int i = 1; i <= T; i++) {
    string s; int K;
    cin >> s;
    cin >> K;
    
    cout << "Case #" << i << ": ";
    int res = solve(s, K);
    if (res == -1) cout << "IMPOSSIBLE" << endl;
    else cout << res << endl;
	}
	return 0;
};

int solve(string s, int K) {
  int res = 0;
  while (true) {
    cerr << "s: " << s << endl;
    int len = s.length();    
    int begin = len;
    for (int i = 0; i < len; i++) {
      if (s[i] == '-') {
        begin = i; break;
      }
    }
    cerr << begin << endl;
    s = s.substr(begin);
    len = s.length();
    if (len < K) break;
    
    for (int i = 0; i < K; i++) {
      if (s[i] == '-') s[i] = '+';
      else s[i] = '-';
    }
    res++;
  }
  
  cerr << "s: " << s << endl;
  if (s.length() == 0) return res;
  else return -1;
}
