#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

const int infinity = 1e9 + 9;

int N, K;
double U;
vector<double> P;

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d %d", &N, &K);
    scanf("%lf", &U);
    P.clear();
    for (int i = 0; i < N; ++i) {
      double _P;
      scanf(" %lf", &_P);
      P.push_back(_P);
    }

    // sort
    sort(P.begin(), P.end());

    // compute
    int i = 1;
    while (i < N) {
      double price = i * (P[i] - P[i - 1]);
      //printf("Price %lf to go to %d\n", price, i);
      if (price <= U)
        U -= price;
      else
        break;
      i++;
    }

    // set (0, 1, ..., i-1) to M
    double M = P[i - 1] + U / i;
    //printf("N=%d, i=%d, M=%lf\n", N, i, M);
    for (int j = 0; j < i; ++j)
      P[j] = M;
    //for (int j = 0; j < N; ++j)
    //  printf(" %lf", P[j]);
    //printf("\n");
    
    // output product
    double product = 1.0;
    for (int i = 0; i < N; ++i)
      product *= P[i];
    printf("Case #%d: %lf\n", Ti, product);
  }
  return 0;
}
