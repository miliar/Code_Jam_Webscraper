#include <iostream>
#include <string>

using namespace std;

string trim(const string &s) {
  string t = "";
  int k = 0;
  int len = s.size();
  while(k < len && s[k] == '0') k ++;
  for(int i = k; i < len; i ++) {
    t += s[i];
  }
  return t;
}

int main() {
  int T, t;
  cin >> T;
  t = 1;
  while(t <= T) {
    string s;
    cin >> s;
    int len = s.size();
    for(int i = len - 1; i > 0; i --) {
      if(s[i - 1] > s[i]) {
	int k = i - 1;
	s[k] -= 1;
	while(k >= 0 && s[k] == '0' - 1) {
	  s[k] = '9';
	  if(k > 0) {
	    s[k - 1] -= 1;
	  }
	  k --;
	}
	for(int j = i; j < len; j ++) s[j] = '9';
      }
    }
    s = trim(s);
    cout << "Case #" << t << ": " << s << endl;
    t ++;
  }
}
