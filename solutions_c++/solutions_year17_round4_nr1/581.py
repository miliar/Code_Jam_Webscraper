#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

const int N = 4;

int cnt[N];

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    memset(cnt, 0, sizeof cnt);
    cout << "Case #" << cs << ": ";
    int n, p;
    cin >> n >> p;

    while (n--) {
      int x;
      cin >> x;
      ++cnt[x % p];
    }

    int res = cnt[0];

    for (int i = 1; i < p; ++i) {
      int j = p - i;

      if (i == j) {
        while (cnt[i] > 1) {
          cnt[i] -= 2;
          ++res;
        }
        continue;
      }

      while (cnt[i] > 0 && cnt[j] > 0) {
        --cnt[i];
        --cnt[j];

        ++res;
      }
    }

    vector<int> rem;
    while (cnt[2]--) {
      rem.push_back(2);
    }

    while (cnt[3]--) {
      rem.push_back(3);
    }

    while (cnt[1]--) {
      rem.push_back(1);
    }

    int curr_left = 0;

    for (int x : rem) {
      if (curr_left == 0) {
        ++res;
      }
      curr_left = (curr_left - x + p) % p;
    }

    cout << res << '\n';
  }

}
