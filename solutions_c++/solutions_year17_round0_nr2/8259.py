#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
  const bool TEST = argc == 2;
  const bool DEBUG = false || TEST;
  int t;
  string n;
  string Y;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if (TEST) { cin >> Y; }
    cout << "Case #" << i << ": ";
    if (DEBUG) { cout << endl; }
    if (DEBUG) { cout << n << endl; }

    int length = n.length();
    int N[length];
    for (int j = 0; j < length; j++) {
      N[j] = n[j] - '0';
      // if (DEBUG) { cout << N[j]; }
    }
    // if (DEBUG) { cout << endl; }

    int firstDecrease = -1;
    int lastIncrease = -1;
    for (int j = 0; j < length-1; j++) {
      if (N[j] > N[j+1]) { firstDecrease = j; break; }
      else if (N[j] < N[j+1]) { lastIncrease = j; }
    }

    // if (DEBUG) {
    //   cout << "last increase: " << lastIncrease << endl;
    //   cout << "first decrease: " << firstDecrease << endl;
    // }

    if (firstDecrease > -1) {
      N[lastIncrease+1] -= 1;
      for (int j = lastIncrease+2; j < length; j++) {
        N[j] = 9;
      }
    }

    if (N[0] != 0) { cout << N[0]; }
    for (int j = 1; j < length; j++) {
      cout << N[j];
    }
    cout << endl;

    if (TEST) {
      for (int j = 0, k = N[0] == 0 ? 1 : 0; j < Y.length(); j++, k++) {
        if (Y[j] - '0' != N[k]) {
          cout << "Y[" << j << "] = " << Y[j] << ", N[" << k << "] = " << N[k] << " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
          break;
        }
      }
    }
  }
}

