#include <iostream>
#include <string>

using namespace std;


int main() {
  int t;
  string n;
  cin >> t;

  for (int i = 1; i <= t; i++) {
    cin >> n;

    for (int j = n.length() - 1; j > 0; j--) {
      if (n[j] < n[j - 1]) {
        for (int k = j; k < n.length(); k++) {
          n[k] = '9';
        }
        n[j - 1]--;
      }
    }

    if (n[0] == '0') n.erase(0, 1);

    cout << "Case #" << i << ": " << n << endl;
  }

  return 0;
}
