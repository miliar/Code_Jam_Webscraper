#include <bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')
typedef long long int lld;
const int NMAX = 1000;

bitset < NMAX + 5 > stalls;

pair<lld, lld> solve(lld N, lld K) {
  stalls = 0;
  stalls[0] = stalls[N + 1] = true;

  lld besti, bestL, bestR;

  while (K--) {
    besti = bestL = bestR = -1;

    for (lld i = 0; i <= N + 1; ++i) {
      if (!stalls[i]) {
        lld L, R;

        for (L = 0; !stalls[i - L]; ++L);
        for (R = 0; !stalls[i + R]; ++R);

        --L, --R;

        if (min(L, R) > min(bestL, bestR)) {
          besti = i;
          bestL = L;
          bestR = R;
        }

        if (min(L, R) == min(bestL, bestR) && max(L, R) > max(bestL, bestR)) {
          besti = i;
          bestL = L;
          bestR = R;
        }
      }
    }

    stalls[besti] = true;
  }

  return {max(bestL, bestR), min(bestL, bestR)};
}

int main() {
  cin.sync_with_stdio(false);

  int num_cases;
  cin >> num_cases;

  lld N, K;
  for (int case_index = 1; case_index <= num_cases; ++case_index) {
    cin >> N >> K;
    pair<lld, lld> sol = solve(N, K);

    cout << "Case #" << case_index << ": ";
    cout << sol.first << " " << sol.second;
    cout << '\n';
  }


  return 0;
}
