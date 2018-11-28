#include <iostream>
#include <vector>
#include <string>
using namespace std;

int processCase(string s, int k) {
  int flips = 0;
  int n = s.size();
  for (int i = 0; i < n - k + 1; i++) {
    if (s[i] == '+') {
      // No-op
      continue;
    }
    flips++;
    for (int j = i; j < i + k; j++) {
      s[j] = (s[j] == '+') ? '-' : '+';
    }
  }

  for (int i = n - k; i < n; i++) {
    if (s[i] == '-') {
      return -1;
    }
  }
  return flips;
}

int main(int args, char* argv[]) {
  int T, K;
  string S;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> S >> K;
    int flips = processCase(S, K);
    if (flips >= 0) {
      cout << "Case #" << t << ": " << flips << endl;
    } else {
      cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
