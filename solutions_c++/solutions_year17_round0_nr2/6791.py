#include <iostream>
#include <string>

using namespace std;

bool is_tidy(string &s) {
  char last = '0';
  for (char c: s) {
    if (c < last)
      return false;
    last = c;
  }
  return true;
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    string n;
    cin >> n;

    if (!is_tidy(n)) {
        for (int j = n.length() - 1; j > 0; j--) {
          if (n[j] < n[j - 1]) {
            n[j - 1] = n[j - 1] - 1;
            for (int k = j; k < n.length(); k++)
              n[k] = '9';
          }
        }
    }

    while (n[0] == '0')
      n.erase(0, 1);

    cout << "Case #" << i + 1 << ": " << n << endl;
    
  }
}
