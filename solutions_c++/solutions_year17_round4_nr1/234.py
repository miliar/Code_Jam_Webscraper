#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef vector<int> Vi;

const int PS = 4;
const int KS = 101;

int dp[PS][KS][KS][KS];
int dpc[PS][KS][KS][KS];
int cv = 0;
int mod;

int fun(int p, Vi& v) {
  int s = 0;
  for (int i = 1; i < int(v.size()); ++i) {
    s += v[i];
  }
  if (s == 0) {
    return v[0];
  }
  int m1 = 1 < v.size() ? v[1] : 0;
  int m2 = 2 < v.size() ? v[2] : 0;
  int m3 = 3 < v.size() ? v[3] : 0;
  if (dpc[p][m1][m2][m3] == cv) {
    return dp[p][m1][m2][m3];
  }
  int res = 0;
  for (int i = 1; i < int(v.size()); ++i) {
    int fresh = p == 0 ? 1 : 0;
    if (v[i] > 0) {
      --v[i];
      res = max(res, fresh + fun((p + i)%mod, v));
      ++v[i];
    }
  }
  dpc[p][m1][m2][m3] = cv;
  dp[p][m1][m2][m3] = res;
  return res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n;
    cin >> n >> mod;
    Vi v(mod, 0);
    for (int i = 0; i < n; ++i) {
      int s;
      cin >> s;
      ++v[s%mod];
    }
    ++cv;
    cout << "Case #" << cas << ": " << fun(0, v) << endl;
  }
}
