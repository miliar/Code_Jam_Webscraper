#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  using namespace std;
  int T;

  cin >> T;
  for (int caseId = 1; caseId <= T; ++caseId) {
    unsigned long long N, K;
    cin >> N >> K;
    cout << "Case #" << caseId << ": ";
    vector<bool> stalls(N + 2, false);
    stalls[0] = true;
    stalls[N + 1] = true;
    int minLsRs;
    int maxLsRs;
    int maxStall;
    for (int person = 0; person < K; ++person) {
      minLsRs = maxLsRs = maxStall = -1;
      for (int i = 1; i <= N; ++i) {
        if (!stalls[i]) {
          int j = i - 1;
          while (!stalls[j]) --j;
          int k = i + 1;
          while (!stalls[k]) ++k;
          int Ls = i - j - 1;
          int Rs = k - i - 1;
          if (min(Ls, Rs) > minLsRs) {
            minLsRs = min(Ls, Rs);
            maxLsRs = max(Ls, Rs);
            maxStall = i;
          } else if (min(Ls, Rs) == minLsRs && max(Ls, Rs) > maxLsRs) {
            maxLsRs = max(Ls, Rs);
            maxStall = i;
          }
        }
      }
      // cout << "Person " << person << ", Stall " << maxStall << endl;
      stalls[maxStall] = true;
    }
    cout << maxLsRs << ' ' << minLsRs << endl;
  }
}
