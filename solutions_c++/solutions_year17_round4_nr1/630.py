#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ul;

int main(int argc, char* argv[]) {
  ios_base::sync_with_stdio(false);
  int tc;
  cin >> tc;
  int dp[101][101][101][101][4];
  for (int current_tc = 1; current_tc <= tc; ++current_tc) {
    int N, P;
    cin >> N >> P;
    vector<int> cnts(P, 0);
    for (ll n = 0; n < N; ++n) {
      ll g;
      cin >> g;
      cnts[g % P]++;
    }
    for (int i0 = cnts[0]; i0 >= 0; --i0)
      for (int i1 = cnts[1]; i1 >= 0; --i1)
        for (int i2 = cnts[2]; i2 >= 0; --i2)
          for (int i3 = cnts[3]; i3 >= 0; --i3)
            for (int p = 0; p < P; ++p) {
              int tmp = 0;
              int carry = p ? 0 : 1;
              if (i0 < cnts[0])
                tmp = max(tmp, carry+dp[i0+1][i1][i2][i3][p]);
              if (i1 < cnts[1])
                tmp = max(tmp, carry+dp[i0][i1+1][i2][i3][(p+1)%P]);
              if (3 <= P && i2 < cnts[2])
                tmp = max(tmp, carry+dp[i0][i1][i2+1][i3][(p+2)%P]);
              if (4 <= P && i3 < cnts[3])
                tmp = max(tmp, carry+dp[i0][i1][i2][i3+1][(p+3)%P]);
//              printf("%d %d %d %d %d (%d)\n", i0, i1, i2, p, tmp, carry);
              dp[i0][i1][i2][i3][p] = tmp;
            }
    ll res = dp[0][0][0][0][0];
    printf("Case #%d: %lli\n", current_tc, res);
  }

  return 0;
}
