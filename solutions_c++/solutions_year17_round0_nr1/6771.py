#include <iostream>
#include <string>
using namespace std;

char flip(char ch) {
  if (ch == '-') return '+';
  return '-';
}

int main() {
  int n;
  cin >> n;
  for (int tc = 1; tc <= n; tc++) {
    string input;
    int k;
    cin >> input >> k;
    int l = input.size();
    int ans = 0;
    for (int idx = 0; idx + k <= l; idx++) {
      if (input[idx] == '+') { continue; }
      ans++;
      for (int j = 0; j < k; j++ ) {
        input[idx + j] = flip(input[idx + j]);
      }
    }

    int check = true;
    for (int i = 0; i < l; i++) {
      if (input[i] == '-') check = false;
    }

    cout << "Case #" << tc << ": ";
    if (check) {
      cout << ans << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}