#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <numeric>
#include <functional>
using namespace std;

typedef unsigned long long int llui;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<string, string> pss;

const int sz = 1e5;

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int N, P;
    cin >> N >> P;
    vector<int> group(N);
    for (int i = 0; i < N; ++i) {
      cin >> group[i];
    }
    vector<int> r(P);
    for (int i = 0; i < N; ++i) {
      int remain = group[i] % P;
      remain = remain > 0 ? P - remain : 0;
      ++r[remain];
    }
    int ans = r[0];

    for (int i = 1; i <= P / 2; ++i) {
      if (i != P - i) {
        int g1 = min(r[i], r[P - i]);
        ans += g1;
        r[i] -= g1;
        r[P - i] -= g1;
      } else {
        ans += r[i] / 2;
        r[i] %= 2;
      }
    }

    if (P == 2) {
      ans += r[1] == 1;
    } else if (P == 3) {
      if (r[2] != 0) {
        ans += (r[2] + 2) / 3;
      } else {
        ans += (r[1] + 2) / 3;
      }
    } else if (P == 4) {
      if (r[1] != 0) {
        if (r[2] > 0) {
          if (r[1] > 2) {
            r[1] -= 2;
            --r[2];
            ++ans;
            ans += (r[1] + 3) / 4;
          } else {
            ++ans;
          }
        } else {
          ans += (r[1] + 3) / 4;
        }
      } else {
        if (r[2] > 0) {
          if (r[3] > 2) {
            r[3] -= 2;
            --r[2];
            ++ans;
            ans += (r[3] + 3) / 4;
          } else {
            ++ans;
          }
        } else {
          ans += (r[3] + 3) / 4;
        }
      }
    }

    cout << ans << endl;
  }
}

