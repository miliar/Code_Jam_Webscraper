#include <iostream>
using namespace std;

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    string s; cin >> s;
    for (int i = s.size()-2; i >= 0; i--) {
      if (s[i] > s[i+1]) {
        s[i]--;
        for (int j=i+1; j < s.size(); j++) s[j] = '9';
      }
    }

    int z = 0;
    while (s[z] == '0' && z+1 < s.size()) z++;
    cout << "Case #" << c << ": " << s.substr(z) << endl;
  }
  return 0;
}
