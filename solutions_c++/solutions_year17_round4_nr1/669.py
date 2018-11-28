#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < (n); ++i)
#define ROF(i, n) for (int i = (n) - 1; i >= 0; --i)
#define REP(i, n) for (int i = 1; i <= (n); ++i)
#define REP3(i, s, n) for (int i = (s); i <= (n); ++i)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int T, N, P;
int G[101], H[4];

int main() {
  cin >> T;
  REP (tc, T) {
    cin >> N >> P;
    H[0] = H[1] = H[2] = H[3] = 0;
    FOR (i, N) {
      cin >> G[i];
      ++H[G[i] % P];
    }

    int ans;
    if (P == 2) {
      int mid = H[1] / 2;
      ans = H[0] + mid;
      if (2 * mid < H[1]) ++ans;
    } else if (P == 3) {
      int m = min(H[1], H[2]);
      H[1] -= m;
      H[2] -= m;
      ans = H[0] + m;
      int k = H[1] / 3;
      int k2 = H[2] / 3;
      ans += k + k2;
      H[1] -= k * 3;
      H[2] -= k2 * 3;
      if (H[1] > 0 || H[2] > 0) ++ans;
    } else if (P == 4) {
      int m = min(H[1], H[3]);
      int mid = H[2] / 2;
      ans = H[0] + m + mid;
      H[1] -= m;
      H[3] -= m;
      H[2] -= 2 * mid;

      int remaining = H[1] + H[3];
      if (H[2] != 0) {
        --H[2];
        remaining -= 2;
        ++ans;
      }
      int k = remaining / 4;
      ans += k;
      remaining -= 4 * k;
      if (remaining > 0) ++ans;
    }

    cout << "Case #" << tc << ": ";
    cout << ans;
    cout << endl;
  }
  return 0;
}
