#include <bits/stdc++.h>

using namespace std;

int solve(string s, int k) {
  vector<int> vec;
  for (auto c : s) {
    vec.push_back(c == '-' ? 0 : 1);
  }
  int num = 0;
  for (int i = 0; i < (int)vec.size(); i++) {
    if (vec[i] == 0) {
      num++;
      if (i + k > vec.size()) {
        return -1;
      }
      for (int j = i; j < i + k; j++) {
        vec[j] ^= 1;
      }
    }
  }
  return num;
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    string s;
    int k;
    cin >> s >> k;
    cout << "Case #" << cas << ": ";
    solve(s, k) == -1 ? cout << "IMPOSSIBLE" << endl
                      : cout << solve(s, k) << endl;
  }
  return 0;
}
