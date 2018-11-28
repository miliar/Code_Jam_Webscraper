#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main() {
  int T, K, ans;
  string S;

  cin >> T;
  for (int t=0; t<T; ++t) {
    cin >> S >> K;

    // O(|S|x|S|) is enough
    ans = 0;
    for (int i=0, l=S.size(); i+(K-1)<l; ++i) {
      if (S[i] == '-') {
        for (int j=0; j<K; ++j) {
          S[i+j] = (S[i+j] == '+') ? '-' : '+';
        }

        ++ans;
      }
    }

    bool possible = true;
    for (auto i: S) possible &= (i == '+');

    cout << "Case #" << t + 1 << ": ";
    if (possible) {
      cout << ans;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }

  return 0;
}
