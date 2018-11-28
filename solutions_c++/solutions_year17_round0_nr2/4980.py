#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  for (int ti = 0; ti < t; ++ti) {
    string s;
    cin >> s;
    bool f1=0, f2=0;
    int lr = 0;
    for (int i = 0; i < s.size()-1; ++i) {
      if (s[i] > s[i+1]) { f1=1; break; }
      if (s[i] != s[i+1]) lr = i+1;
    }
    cout << "Case #" << ti+1 << ": ";
    for (int i = 0; i < s.size(); ++i) {
      if (f2) cout << 9;
      else if (f1 && lr == i) {
        if (char(s[i]-1) != '0') cout << char(s[i]-1);
        f2 = 1;
      } else cout << s[i];
    }
    cout << endl;
  }
}
