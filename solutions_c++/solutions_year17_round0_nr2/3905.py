#include <iostream>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    string s;
    cin >> s;
    int digits[s.length()];
    for (int i = 0; i < s.length(); i++)
      digits[i] = s[i]-'0';

    for (int i = 1; i < s.length(); i++)
      if (digits[i] < digits[i-1]) {
        for (int j = i+1; j < s.length(); j++) digits[j] = 9;
        while (i >= 1 && digits[i] < digits[i-1]) {
          digits[i-1]--;
          digits[i] = 9;
          i--;
        }
        break;
      }

    cout << "Case #" << t << ": ";
    int i = 0;
    if (digits[i] == 0) i++;
    for (; i < s.length(); i++) cout << digits[i];
    cout << "\n";
  }

  return 0;
}
