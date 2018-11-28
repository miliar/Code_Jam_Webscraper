#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  stringstream output;
  cin >> T;
  for (int ii = 0; ii < T; ++ii) {
    int N, K;
    cin >> N >> K;
    int gap = 2 * N, pow2 = 1, unplaced = K, popBig = 1, popSmall = 0, popSmallLast = 0;
    // Take sum base2 of K, halve the gap size each time...
    while (unplaced - pow2 >= 0) {
      unplaced -= pow2;
      gap /= 2;
      // If gap is even, popSmall increases. Else popBig does
      if (gap % 2 == 0) {
	popSmallLast = popSmall;
	popSmall += pow2;
      } else {
	popBig += pow2;
      }
      pow2 *= 2;
    }
    if (unplaced > 0) gap /= 2;
    // If there are more people left than large gaps, the last person is inserted into a small gap.
    if (unplaced > popBig || (unplaced == 0 && popSmallLast > 0)) gap--;
    // If gap was odd, minS is one less.
    int maxS = gap / 2;
    int minS = maxS;
    if (gap % 2 == 0) minS--;
    output << "Case #" << ii + 1 << ": " << maxS << " " << minS << endl;
  }
  cout << output.str();
  return 0;
}
