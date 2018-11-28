#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
  int T;
  int N,K;
  double U, P[50];

  cin >> T;

  for(int tc = 1;tc <= T;++tc){
    cin >> N >> K >> U;

    double ans = 1;

    for(int i = 0;i < N;++i){
      cin >> P[i];
      ans *= P[i];
    }

    sort(P,P + N);

    for(int i = 0;i < N;++i){
      double x = U;

      for(int j = 0;j <= i;++j){
        x += P[j];
      }

      x /= (1 + i);
      x = min(x,1.0);

      if(x >= P[i]){
        double aux = 1;
        for(int j = 0;j <= i;++j) aux *= x;
        for(int j = i + 1;j < N;++j) aux *= P[j];
        ans = max(ans, aux);
      }
    }

    printf("Case #%d: %.8f\n", tc, ans);
  }

  return 0;
}
