#include <iostream>
using namespace std;

const bool DEBUG = false;

int main() {
  int t;
  string s;
  int k;
  int Y;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> s >> k;
    if (DEBUG) { cin >> Y; }
    cout << "Case #" << i << ": ";

    int length = s.length();
    int S[length];
    for (int j = 0; j < length; j++) {
      S[j] = s[j] == '+' ? 1 : -1;
    }

    if (DEBUG) { cout << endl << "0, " << s << endl; }

    int y = 0;
    for (int j = 0; j < length; j++) {
      if (S[j] == -1 && j+k-1 < length) {
        y++;
        for (int m = 0; m < k; m++) {
          S[j+m] *= -1;
          if (DEBUG) { s[j+m] = S[j+m] == 1 ? '+' : '-'; }
        }
        if (DEBUG) cout << y << ", " << s << endl;
      }
    }

    bool good = true;
    for (int j = 0; j < length; j++) {
      if (S[j] == -1) {
        good = false;
        break;
      }
    }

    if (good) {
      cout << y;
    } else {
      y = -1;
      cout << "IMPOSSIBLE";
    }
    cout << endl;

    if (DEBUG) {
      if (y != Y) {
        cout << "y: " << y << ", Y: " << Y << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
      }
    }
  }
}

