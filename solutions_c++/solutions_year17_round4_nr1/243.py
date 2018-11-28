// C++11
#include <cstdio>
#include <algorithm>
using namespace std;

// P=2: 0 or 1+1
// P=3: 0 or 1+2 or 1+1+1 or 2+2+2
// P=4: 0 or 2+2 or 1+3 or 1+1+2 or 2+3+3 or 1+1+1+1 or 3+3+3+3

int main() {
  int T; scanf("%d", &T);
  for(int tci = 0; tci < T; ++tci) {
    int N, P; scanf("%d%d", &N, &P);
    int modcount[4] = {0, 0, 0, 0};
    int sum = 0;
    for(int i = 0; i < N; ++i) {
      int G;
      scanf("%d", &G);
      G %= P;
      ++modcount[G];
      sum = (sum + G) % P;
    }
    int count = 1 - (sum == 0) + modcount[0];
    if(P == 2 || P == 4) {
      count += modcount[P/2] / 2;
      modcount[P/2] %= 2;
    }
    if(P == 3 || P == 4) {
      int u = min(modcount[1], modcount[P-1]);
      count += u;
      modcount[1] -= u;
      modcount[P-1] -= u;
    }
    if(P == 4 && modcount[2] == 1) {
      if(modcount[1] >= 2) {
        count++;
        modcount[1] -= 2;
      } else if(modcount[3] >= 2) {
        count++;
        modcount[3] -= 2;
      }
    }
    if(P == 3 || P == 4) {
      count += modcount[1]/P;
      count += modcount[P-1]/P;
    }
    printf("Case #%d: %d\n", tci + 1, count);
  }
  return 0;
}
