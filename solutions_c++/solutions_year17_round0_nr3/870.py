#include <iostream>
#include <inttypes.h>
#include <cassert>

using namespace std;

void solve(uint64_t N, uint64_t K) {
  uint64_t maxV = N, minV = 0;
  uint64_t maxC = 1, minC = 0;
  while ((maxC + minC) < K) {
    K -= (maxC + minC);
    assert (minC == 0 || maxV == minV + 1); --maxV; --minV;
    uint64_t newMaxV = 0, newMinV = 0, newMaxC = 0, newMinC = 0;
    uint64_t maxSmall = maxV >> 1, maxLarge = maxV - maxSmall;
    if (maxSmall == maxLarge) { newMaxV = maxSmall; newMaxC = maxC << 1; }
    else { newMaxV = maxLarge; newMinV = maxSmall; newMaxC = newMinC = maxC; }
    if (minC) {
      uint64_t minSmall = minV >> 1, minLarge = minV - minSmall;
      if (minSmall == minLarge) {
        assert (newMinC == 0 || minSmall == newMinV);
        newMinV = minSmall; newMinC += (minC << 1);
      }
      else {
        assert (maxSmall == newMaxV);
        assert (newMinC == 0 || minSmall == newMinV);
        newMinV = minSmall; newMaxC += minC; newMinC += minC;
      }
    }
    maxV = newMaxV; minV = newMinV; maxC = newMaxC; minC = newMinC;
    //cout << "Consider: " << (maxC + minC) << ": Max: " << maxV << " (" << maxC << "), Min: " << minV << " ( " << minC << ")" << endl;
  }
  uint64_t min, max; --maxV; --minV;
  if (K <= maxC) min = maxV >> 1, max = maxV - min;
  else min = minV >> 1, max = minV - min;
  cout << max << " " << min;
}

int main() {
  uint64_t T; cin >> T;
  for (uint64_t i = 1; i <= T; ++i) {
    uint64_t N, K; cin >> N >> K;
    cout << "Case #" << i << ": "; solve(N, K); cout << endl;
  }
  return 0;
}

