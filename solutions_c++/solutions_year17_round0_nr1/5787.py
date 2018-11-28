#include <iostream>
#include <string>
using namespace std;

string solve(string& s, int k) {
  int n = s.size(), count = 0;
  for (int i = 0; i < n - k + 1; i++) {
    if (s[i] == '+') continue;

    for (int j = i; j < i + k; j++) {
      s[j] = (s[j] == '+' ? '-' : '+');
    }
    count++;
  }
  if (s.find('-') != string::npos) {
    return "IMPOSSIBLE";
  } else {
    return to_string(count);
  }
}

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    string s;
    int k;
    cin >> s >> k;
    cout << "Case #" << i << ": " << solve(s, k) << endl;
  }
  return 0;
}