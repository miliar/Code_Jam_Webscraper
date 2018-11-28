#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstdio>

using namespace std;

long long floor_tidy(long long N) {
  string s = to_string(N);
  for (int i = 1; i < s.size(); i++) {
    if (s[i] < s[i - 1]) {
      string t = s;
      for (int j = i; j < s.size(); j++) {
        t[j] = s[i - 1];
      }
      if (t <= s) {
        return stoll(t);
      }
      long long r = floor_tidy(stoll(s.substr(0, i)) - 1);
      for (int j = i; j < s.size(); j++) {
        r = r * 10 + 9;
      }
      return r;
    }
  }
  return N;
}

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N;
    cin >> N;
    cout << "Case #" << t << ": " << floor_tidy(N) << endl;
  }
  return 0;
}
