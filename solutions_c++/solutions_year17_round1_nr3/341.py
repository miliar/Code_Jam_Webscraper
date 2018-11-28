#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
#define inf 0x3f3f3f3f

#define MAX 102
int dp[MAX][MAX][MAX][MAX];

typedef tuple<int, int, int, int> t4i;

int hd, ad, hk, ak, b, d;
int orig_hd;

int solve(int hd, int ad, int hk, int ak) {
  if (dp[hd][ad][hk][ak] == -1) {
    dp[hd][ad][hk][ak] = -2;

    int nhd, nad, nhk, nak;
    int ans = inf;

    if (hk == 0) {
      ans = 0;
    } else if (hd == 0) {
      ;  // nothing
    } else {
      /* debuff */
      nak = max(ak - d, 0);
      nhk = hk;
      nad = ad;
      nhd = max(hd - nak, 0);

      if (nhd != hd || nad != ad || nhk != hk || nak != ak) {
        if (dp[nhd][nad][nhk][nak] != -2) {
          ans = min(ans, 1 + solve(nhd, nad, nhk, nak));
        }
      }

      /* buff */
      nak = ak;
      nhk = hk;
      nad = min(ad + b, 100);
      nhd = max(hd - nak, 0);

      if (nhd != hd || nad != ad || nhk != hk || nak != ak) {
        if (dp[nhd][nad][nhk][nak] != -2) {
          ans = min(ans, 1 + solve(nhd, nad, nhk, nak));
        }
      }

      /* heal */
      nak = ak;
      nhk = hk;
      nad = ad;
      nhd = max(orig_hd - nak, 0);

      if (nhd != hd || nad != ad || nhk != hk || nak != ak) {
        if (dp[nhd][nad][nhk][nak] != -2) {
          ans = min(ans, 1 + solve(nhd, nad, nhk, nak));
        }
      }

      /* attack */
      nak = ak;
      nad = ad;
      nhk = max(hk - nad, 0);
      nhd = max(hd - nak, 0);

      if (nhd != hd || nad != ad || nhk != hk || nak != ak) {
        if (dp[nhd][nad][nhk][nak] != -2) {
          ans = min(ans, 1 + solve(nhd, nad, nhk, nak));
        }
      }
    }
    return dp[hd][ad][hk][ak] = ans;

  } else {
    return dp[hd][ad][hk][ak];
  }
}

int main() {
  ios ::sync_with_stdio(0);

  int t;
  cin >> t;
  for (int cn = 1; cn <= t; cn++) {
    cin >> hd >> ad >> hk >> ak >> b >> d;

    orig_hd = hd;
    memset(dp, -1, sizeof(dp));

    int best = solve(hd, ad, hk, ak);

    if (best >= inf) {
      printf("Case #%d: IMPOSSIBLE\n", cn);
    } else {
      printf("Case #%d: %d\n", cn, best);
    }
  }

  return 0;
}
