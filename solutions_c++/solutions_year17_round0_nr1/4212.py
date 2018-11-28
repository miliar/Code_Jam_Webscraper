#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

char flipCharParity(char c) {
  if (c == '+') return '-';
  if (c == '-') return '+';
  return 'e';
}

void flipSubstringParity(string& s, int num, int start) {
  for (int i = 0; i < num; ++i) {
    s[i + start] = flipCharParity(s[i + start]);
  }
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    string s;
    cin >> s;
    int K;
    cin >> K;

    int numFlips = 0;

    for (int i = 0; i < s.length() - K + 1; ++i) {
      char c = s[i];
      if (c == '-') {
        flipSubstringParity(s, K, i);
        numFlips++;
      }

    }

    bool success = true;

    for (int i = 0; i < K; ++i) {
      if (s[s.length() - 1 - i] == '-') {
        success = false;
        break;
      }
    }

    if (success) cout << "Case #" << t << ": " << numFlips << endl;
    else cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
  }
  return 0;
}
