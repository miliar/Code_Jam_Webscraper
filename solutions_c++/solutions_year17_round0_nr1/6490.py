#include <iostream>

using namespace std;

int main() {
  int t;

  cin >> t;

  for (int a = 0; a < t; a++) {
    string s;
    int k;

    cin >> s;
    cin >> k;

    int i = 0;
    int size = s.size();
    int moves = 0;

    while (i <= size - k) {
      if (s[i] == '-') {
        moves++;
        s[i] = '+';
        for (int j = i + 1; j < i + k; j++) {
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
      }
      i++;
    }

    bool face_up = true;
    for (; i < size; i++) {
      if (s[i] == '-') {
        face_up = false;
        break;
      }
    }

    if (face_up) {
      cout << "Case #" << a + 1 << ": " << moves << endl;
    } else {
      cout << "Case #" << a + 1 << ": " << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}