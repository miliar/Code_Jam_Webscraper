#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
  vector<int> fryer;
  int T, K, l, m;
  char c = 0;
  bool impossible = false;

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    fryer.clear();
    m = 0;
    c = 0;
    impossible = false;
    cin >> c;
    while (c != 43 && c != 45) {
      cin.read(&c, 1);
      cout << "We shouldn't be here.";
    }
    while (c != 32) {
      if (c == 43) {
        fryer.push_back(1);
      } else if (c == 45) {
        fryer.push_back(0);
      } else {
        cout << "Error 1." << endl;
      }
      cin.read(&c, 1);
    }
    cin >> K;

    if (K < 1) {
      cout << "Error 2." << endl;
    }

    l = fryer.size();
    for (int j = 0; j < l - K + 1; ++j) {
      if (fryer[j] == 0) {
        ++m;
        for (int k = j; k < j + K; ++k) {
          fryer[k] = 1 - fryer[k];
        }
      }
    }
    //for (int o = 0; o < fryer.size(); ++o) cout << "fryer[" << o << "] = " << fryer[o] << endl;
    for (int j = l - K + 1; j < l; ++j) {
      if (fryer[j] == 0) {
        impossible = true;
      }
    }

    cout << "Case #" << i << ": ";
    if (impossible) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << m << endl;
    }
  }

  return 0;
}
