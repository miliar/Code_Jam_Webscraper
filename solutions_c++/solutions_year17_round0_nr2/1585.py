#include <iostream>
using namespace std;

void set9(string& s, int i) {
  int n = s.size();
  for (int j = i; j < n; ++j) {
    s[j] = '9';
  }
}

string fun(string s) {
  int n = s.size();
  bool c = false;
  for (int i = n - 2; i >= 0; --i) {
    if (c || s[i] > s[i + 1]) {
      if (s[i] == '0') {
        set9(s, i);
        c = true;
      } else {
        --s[i];
        set9(s, i + 1);
        c = false;
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    if (s[i] != '0') {
      return s.substr(i);
    }
  }
  return "";
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    string s;
    cin >> s;
    cout << "Case #" << cas << ": " << fun(s) << endl;
  }
}
