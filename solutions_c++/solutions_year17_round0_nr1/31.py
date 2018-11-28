#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define DEBUG
#ifdef DEBUG
#define TRACE(x) cerr << #x << " = " << x << endl;
#define _ << " _ " <<
#else
#define TRACE(x) ((void)0)
#endif

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    int ans = 0, k;

    string s;
    cin >> s >> k;
    const int n = s.size();
    for (int i = 0; i + k <= n; i++) {
      if (s[i] == '-') {
        for (int j = 0; j < k; j++)
          s[i + j] = s[i + j] == '+' ? '-' : '+';
        ans++;
      }
    }

    cout << "Case #" << tt << ": ";
    bool good = true;
    for (int i = 0; i < n; i++)
      if (s[i] == '-') {
        cout << "IMPOSSIBLE";
        good = false;
        break;
      }
    if (good)
      cout << ans;
    cout << '\n';
  }

  return 0;
}
