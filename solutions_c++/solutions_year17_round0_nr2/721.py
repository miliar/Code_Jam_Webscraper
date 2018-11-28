#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T; 
  for (int i = 0; i < T; i++) {
    string s;
    cin >> s;
    char prev = '0';
    int k = -1;
    for (int j = 0; j < s.size(); j++) {
      if (s[j] > prev) {
        k = j;
        prev = s[j];
      }
      if (s[j] < prev) {
        if (prev == '1') {
          for (char& c : s) c = '9';
          s[0] = '0';
        } else {
          s[k] = prev-1;
          for (int p = k+1; p < s.size(); p++) {
            s[p] = '9';
          }
        }
        break;
      }
    }
    cout << "Case #" << i+1 << ": ";
    for (char c : s)
      if (c != '0') cout << c;
    cout << endl;
  }
  return 0;
}
