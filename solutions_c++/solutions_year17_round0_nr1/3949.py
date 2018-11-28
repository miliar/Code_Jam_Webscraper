#include <iostream>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string s;
    int k;
    cin >> s >> k;

    int numOfFlips = 0;
    for (int i = 0; i <= s.length()-k; i++) {
      // cout << i << " " << s << "\n";
      if (s[i] == '-') {
        for (int j = i; j < i+k; j++)
          if (s[j] == '-') s[j] = '+';
          else s[j] = '-';
        numOfFlips++;
      }
    }
    // cout << s << "\n";

    bool possible = true;
    for (int i = 0; i < s.length(); i++)
      if (s[i] == '-') possible = false;

    if (possible) cout << "Case #" << t << ": " << numOfFlips << "\n";
    else cout << "Case #" << t << ": IMPOSSIBLE\n";
  }

  return 0;
}
