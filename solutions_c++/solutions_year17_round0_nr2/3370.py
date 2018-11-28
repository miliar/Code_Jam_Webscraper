#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void output(int t, string res) {
  cout << "Case #" << t + 1<< ": " << res << endl;
}

int main() {
  int t;
  cin >> t;
  for (int tt = 0; tt < t; tt++) {
    unsigned long long n;
    cin >> n;
    stringstream ss;
    ss << n;
    string s = ss.str();
    int len = s.length();
    int i;
    for (i=0; i < len - 1; i++) {
      if (s[i] > s[i+1]) break;
    }
    if (i < len -1) {
      if (s[i] > '1') {
        while(i>0 && s[i]==s[i-1]) i--;
        s[i] -= 1;
        for (int j = i+1; j < len; j++) {
          s[j] = '9';
        }
        output(tt, s);
      } else {
        string res(len - 1, '9');
        output(tt, res);
      }
    } else {
      output(tt, s);
    }
  }
  return 0;
}
