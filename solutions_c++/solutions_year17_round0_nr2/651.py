#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

int main() {

  int T;
  cin >> T;

  for (int tc = 1; tc <= T; tc++) {
    string n;
    cin >> n;

    n = "0" + n;

    ull ans = is_sorted(n.begin(), n.end()) ? stoull(n) : 0ULL;

    for (int i = 0; i < n.size(); i++) {
      if (n[i] != '0') {
        string n2 = n;
        n2[i]--;

        for (int j = i+1; j < n2.size(); j++)
          n2[j] = '9';

        for (int j = i-1; j >= 0; j--)
          n2[j] = min(n2[j], n2[j+1]);

        ans = max(ans, stoull(n2));
      }
    }

    cout << "Case #" << tc << ": " << ans << endl;
  }

  return 0;
}
