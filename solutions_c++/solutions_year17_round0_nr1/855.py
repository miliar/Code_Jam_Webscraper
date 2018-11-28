#include <iostream>
#include <string>
#include <vector>

#include <inttypes.h>

using namespace std;

void solve(string S, uint64_t K) {
  uint64_t flips = 0;
  for (uint64_t i = 0; i < S.size(); ++i) {
    if (S[i] == '-') {
      if (i + K <= S.size()) {
        for (uint64_t j = i, k = 0; k < K; ++j, ++k) S[j] = (S[j] == '-') ? '+' : '-';
        ++flips;
      }
      else {
        cout << "IMPOSSIBLE";
        return;
      }
    }
  }
  cout << flips;
}

int main() {
  uint64_t T; cin >> T;
  for (uint64_t i = 0; i < T; ++i) {
    string S; uint64_t K; cin >> S >> K;
    cout << "Case #" << (1 + i) << ": ";
    solve(S, K);
    cout << endl;
  }
  return 0;
}
