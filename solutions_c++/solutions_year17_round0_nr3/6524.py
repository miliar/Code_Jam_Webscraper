#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  int T, C;

  scanf("%d", &T);
  for(C=1; C<=T; C++) {
    long long int N, K;
    scanf("%lld %lld", &N, &K);

    int M;
    long long int L, R;

    if(N == K) {
      L = R = 0;
      printf("Case #%d: %d %d\n", C, std::max(L, R), std::min(L, R));
      continue;
    }

    vector<long long int> X;
    X.push_back(N);

    do {
      int c = 0;
      int W = 0L;

      for(int i=0; i < X.size(); i++) {
        if(W < X[i]) {
          c = i;
          W = X[i];
          //X.erase(X.begin() + i);
        }
      }

      X.erase(X.begin() + c);

      if(W % 2) {
        L = R = (W - 1) / 2;
        X.push_back(L);
        X.push_back(R);
      } else {
        R = W / 2;
        L = R - 1;
        X.push_back(L);
        X.push_back(R);
      }

      K--;
    } while(K);

    printf("Case #%d: %d %d\n", C, std::max(L, R), std::min(L, R));
  }
  return 0;
}
