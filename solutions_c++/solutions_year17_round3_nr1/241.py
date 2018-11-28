#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int infinity = 1e9 + 9;
const long double PI = 3.141592653589793238L;

int N;
int K;
vector<long long> R;
vector<long long> H;

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%d %d", &N, &K);
    R.clear();
    H.clear();
    for (int i = 0; i < N; ++i) {
      long long _R, _H;
      scanf("%lld %lld", &_R, &_H);
      R.push_back(_R);
      H.push_back(_H);
    }

    // find maximum arrangement before multiplying by pi
    long long maximum = 0;
    for (int i = 0; i < N; ++i) {
      // obtain available products
      vector<long long> P;
      for (int j = 0; j < N; ++j)
        if ((j != i) && (R[j] <= R[i]))
          P.push_back(R[j] * H[j]);
      if (P.size() < K - 1)
        continue;

      // compute (K-1) largest products + R[i] * H[i]
      sort(P.begin(), P.end());
      reverse(P.begin(), P.end());
      long long sum = R[i] * H[i];
      for (int k = 0; k < K - 1; ++k)
        sum += P[k];

      // update maximum
      long long proposal = R[i] * R[i] + 2 * sum;
      if (maximum < proposal)
        maximum = proposal;
    }

    // compute
    long double area = PI * (long double)maximum;
    printf("Case #%d: %Lf\n", Ti, area);
  }
  return 0;
}
