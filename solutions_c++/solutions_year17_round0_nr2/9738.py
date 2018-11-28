#include <iostream>

using namespace std;

string findHighestTidy(string before) {
    string n = before;
    if (n.length() == 1) {
        return n;
    }

    for (int j=1; j < n.length(); j++) {
        if (n[j-1] > n[j]) {
            int pivot = j-1;
            for (int k=pivot; k > 0; k--) {
                if (n[k] == n[k-1]) {
                    pivot = k-1;
                } else {
                    break;
                }
            }
            n[pivot]--;
            pivot++;
            for (int k=pivot; k < n.length(); k++) {
                n[k] = '9';
            }
            break;
        }
    }

    for (int j=0; j < n.length(); j++) {
      if (n[j] != '0') {
        if (j != 0) {
          n.erase(0, j);
        }
        break;
      }
    }
    return n;
}

int main() {
  int c;
  cin >> c;
  for (int i = 1; i <= c; ++i) {
    string tidy;
    cin >> tidy;
    cout << "Case #" << i << ": " << findHighestTidy(tidy) << endl;
  }
  return 0;
}
