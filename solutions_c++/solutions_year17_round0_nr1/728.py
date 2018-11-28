#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    string s;
    int K;
    cin >> s >> K;
    int r = 0;
    for (int j = 0; j < s.size(); j++) {
      if (s[j] == '+') continue;
      if (j + K - 1 >= s.size()) {
        r = -1;
        break;
      }
      r += 1;
      for (int w = j; w < j + K; w++) {
        s[w] = (s[w] == '+' ? '-' : '+');
      }
    }
    cout << "Case #" << i+1 << ": ";
    if (r < 0)
      cout << "IMPOSSIBLE";
    else
      cout << r;
    cout << endl;
  }
  return 0;
}
