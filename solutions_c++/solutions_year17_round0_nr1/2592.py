#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

const char PLUS = '+';
const char MINUS = '-';

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    string s;
    int k;
    cin >> s >> k;
    const int n = s.length();
    int ans = 0;
    for (int i = 0; i + k - 1 < n; ++i) {
      if (s[i] == MINUS) {
        ++ans;
        for (int j = i; j < i + k; ++j)
          s[j] = s[j] == MINUS ? PLUS : MINUS;
      }
    }
    bool ok = true;
    for (char c : s)
      ok &= (c == PLUS);
    cout << "Case #" << test << ": " << (ok ? to_string(ans) : "IMPOSSIBLE") << endl;
  }

  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
