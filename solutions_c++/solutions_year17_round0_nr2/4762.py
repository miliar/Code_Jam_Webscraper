#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string n;
    cin >> n;
    int pos;
    for (pos = 1; n[pos - 1] <= n[pos] && pos < (int)n.length(); ++pos);
    if (pos < (int)n.length()) {
      int prev;
      for (prev = pos - 1; prev > 0 && n[prev - 1] == n[prev]; --prev);
      n[prev]--;
      for (++prev; prev < (int)n.length(); ++prev)
        n[prev] = '9';
      if (n[0] == '0')
        n.erase(0, 1);
    }
    cout << "Case #" << t << ": " << n << endl;
  }
  return 0;
}