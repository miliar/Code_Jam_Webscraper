#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int q = 1; q <=t; q++) {
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    bool pancakes[n];
    for (int i = 0; i < n; i++) {
      pancakes[i] = (s[i] == '+');
    }
    int flips = 0;
    for (int i = 0; i <= n - k; i ++) {
      if (!pancakes[i]) {
        flips++;
        for (int j = i; j < i + k; j++) {
          pancakes[j] = (!pancakes[j]);
        }
      }
    }
    bool ok = true;
    for (int i = n - k + 1; i < n; i++) {
      if (!pancakes[i]) {
        ok = false;
        break;
      }
    }
    cout << "Case #" << q << ": ";
    if (!ok) {
      cout << "IMPOSSIBLE";
    } else {
      cout << flips;
    }
    cout << endl;
  }
}
