#include <bits/stdc++.h>
using namespace std;

const int DAY_MINUTES = 1440;
const int PARENT_MINUTES = DAY_MINUTES / 2;

int A[DAY_MINUTES];

int dp[DAY_MINUTES][PARENT_MINUTES + 1][2][3];

int solve(int curMinute, int cMinutes, bool last, int first) {
  if (curMinute == DAY_MINUTES)
    return last == (first - 1) ? 0 : 1;
  int &ret = dp[curMinute][cMinutes][last][first];
  if (ret != -1) return ret;
  int pMinutes[2] = {cMinutes, curMinute - cMinutes};
  ret = DAY_MINUTES * 44;
  for (int i = 0; i < 2; ++i) {
    if (pMinutes[i] == PARENT_MINUTES) continue;
    if (A[curMinute] > 0 && A[curMinute] - 1 == i) continue;
    ret = min(ret, (first > 0 && last != i) + solve(curMinute + 1, cMinutes + (i == 0 ? 1 : 0), i, first == 0 ? i + 1 : first));
  }
  return ret;
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  int cases; cin >> cases;
  for (int cc = 0; cc < cases; ++cc) {
    cout << "Case #" << cc + 1 << ":";

    int Ac, Aj; cin >> Ac >> Aj;
    memset(A, 0, sizeof(A));
    for (int i = 0; i < Ac + Aj; ++i) {
      int c, d; cin >> c >> d;
      for (int j = c; j < d; ++j)
        A[j] = i < Ac ? 1 : 2;
    }

    memset(dp, -1, sizeof(dp));

    cout << " " << solve(0, 0, 0, 0) << "\n";
  }
  return 0;
}
