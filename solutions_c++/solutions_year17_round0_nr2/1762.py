#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int tst = 0; tst < T; tst++) {
    string s;
    cin >> s;
    int n = int(s.size());

    for (int i = n; i >= 0; i--) {
      bool good = true;

      for (int j = 0; j < i - 1; j++) {
        if (s[j] > s[j + 1]) {
          good = false;
        }
      }

      if (i < n && i > 0 && s[i] <= s[i - 1]) {
        good = false;
      }

      if (good) {
        if (i < n) {
          s[i]--;
        }

        for (int j = i + 1; j < n; j++) {
          s[j] = '9';
        }

        while (s[0] == '0') {
          s.erase(s.begin());
        }
        break;
      }
    }

    cout << "Case #" << tst + 1 << ": " << s << '\n';
  }
}
