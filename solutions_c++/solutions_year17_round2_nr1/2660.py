#include <iostream>
#include <stdio.h>
using namespace std;


int T, D, N, K, S;

int main(int argc, char** argv) {
  cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> D >> N;
    double ans = 0;
    for (int n = 0; n < N; ++n) {
      cin >> K >> S;
      double tim = (double)(D-K) / (double)S;
      if (n==0) ans = tim;
      ans = max(tim,ans);
    }
    printf("Case #%d: %0.9f\n", t+1, (double)D/ans);
  }
}
