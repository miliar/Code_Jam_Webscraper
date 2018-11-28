#include <iostream>
#include <string>

using namespace std;

string max1(int x) {
  return to_string(x);
}

string max2(int x, int y) {
//  cout << "aaa " << x << "**" << y << endl;
  if (x == 1 && y == 0) return "9";
  if (x <= y) return to_string(x) + to_string(y);
  if (to_string(x - 1) == "0") {
    return to_string(9);
  } else {
    return to_string(x - 1) + to_string(9);
  }
}

string maxg(string cad) {
  string ans = "";
  for (int i = cad.length() - 1; i >= 2; i--) {
//    cout << "-- " << i << endl;
    ans = "9" + ans;
  }
  string max2s = max2(cad[0] - '0', cad[1] - '0' - 1);
  return max2s + ans;
}

bool already(string cad) {
  for (int i = 0; i < cad.length() - 1; i++) {
    if ((cad[i] - '0') > (cad[i + 1] - '0')) return false;
  }
  return true;
}

int main() {
  int T;
  cin >> T;

  for (int tc = 1; tc <= T; tc++) {
    string cad;
    cin >> cad;

    if (cad.length() == 1) {
      cout << "Case #" << tc << ": " << cad << endl;
    } else {
      if (already(cad)) {
        cout << "Case #" << tc << ": " << cad << endl;
      } else {
        cout << "Case #" << tc << ": " << maxg(cad) << endl;
      }
    }

  }


  return 0;
}
