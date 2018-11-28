#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void output(int t, string res) {
  cout << "Case #" << t + 1<< ": " << res << endl;
}

void output(int t, int res) {
  cout << "Case #" << t + 1<< ": " << res << endl;
}

int main() {
  int t;
  cin >> t;
  for (int tt = 0; tt < t; tt++) {
    string s;
    cin >> s;
    int k;
    cin >> k;
    int i=0;
    int count = 0;
    while(true) {
      while(s[i] == '+') {
        i++;
      }
      //cout << i << endl;
      if (i >= s.length()) {
        output(tt, count);
        break;
      }
      if (i > s.length() - k) {
        output(tt, "IMPOSSIBLE");
        break;
      }
      for (int j = i; j < i+k; j++) {
        if (s[j] == '-') s[j] = '+';
        else s[j] = '-';
      }
      count++;
      i++;
    }
  }
  return 0;
}
