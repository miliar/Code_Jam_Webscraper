#include <iostream>
#include <string>

using namespace std;

int main() {
  int T, K;
  string S;

  cin >> T;

  for (int i = 0; i < T; i++) {
    cin >> S;
    cin >> K;

    int len = S.length();
    int c = 0;

    for (int j = 0; j < len - K + 1; j++) {
      if (S.at(j) == '-') {
        c++;

        for (int k = 0; k < K; k++) {
          if (S.at(j+k) == '-')
            S.at(j+k) = '+';
          else
            S.at(j+k) = '-';
        }
        //cout << "j: " << j << " => " << S << endl;
      }
    }

    bool possible = true;
    for (int j = len - K +1; j < len; j++) {
      if (S.at(j) == '-') {
        possible = false;
        break;
      }
    }

    if (possible == true)
      cout << "Case #" << (i + 1) << ": " << c << endl;
    else
      cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
  }

  return 0;
}