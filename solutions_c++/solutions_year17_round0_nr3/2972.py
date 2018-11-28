#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    long long n, k;
    cin >> n >> k;

    map<long long, long long> m;
    m[n] = 1;

    long long ans_l = -1, ans_r = -1;
    while (m.size()) {
      auto it = m.rbegin();
      auto length = (*it).first;
      auto cnt = (*it).second;
      m.erase(length);

      auto a = (length - 1) / 2;
      auto b = (length - 1) - a;

      if (a) m[a] += cnt;
      if (b) m[b] += cnt;

      k -= cnt;
      if (k <= 0) {
        ans_l = max(a, b);
        ans_r = min(a, b);
        break;
      }
    }

    assert(ans_l >= 0 and ans_r >= 0);
    cout << ans_l << " " << ans_r << endl;
  }

  return 0;
}
