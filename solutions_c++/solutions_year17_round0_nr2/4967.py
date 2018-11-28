#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;

int ch(char a) {
  return (a - '0');
}

int main() {
  ios_base::sync_with_stdio(false);
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    string s; cin >> s;
    vector<int> a(18);
    int n = s.size();
    if (n == 1) {
      cout << "Case #" << i << ": " << s << endl;
      continue;
    }
    for (int j = 0; j < n; ++j) a[j] = ch(s[j]);

    for (int k = 0; k < 18; ++k) {
      for (int j = 1; j < n; ++j) {
        if (a[j] < a[j - 1]) {
          a[j - 1]--;
          for (int l = j; l < n; ++l) a[l] = 9;
        }
      }
    }

    int j = (a[0] == 0) ? 1 : 0;
    cout << "Case #" << i << ": ";
    for (; j < n; ++j) cout << a[j];
    cout << endl;
  }

  return 0;
}
