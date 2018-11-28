#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <cstring>

using namespace std;

int main()
{
  int T; scanf("%d\n", &T);
  for (int ii = 1; ii <= T; ++ii)
  {
    int D, N;
    scanf("%d %d\n", &D, &N);
    std::vector<int> K(N), S(N);
    for (int i = 0; i < N; ++i)
      scanf("%d %d\n", &(K[i]), &(S[i]));

    double low = 0;
    double high = (2 * (double)D * (double)(S[0])) / ((double)D - (double)(K[0]));

    int count = 0;
    while (high - low > 1e-8 && count < 1000000)
    {
      const double mid = (high + low) / 2;
      bool found = false;
      ++count;

      for (int i = 0; i < N; ++i)
      {
        if (mid <= S[i]) continue;
        if (K[i] * mid >= (mid-S[i]) * D) continue;
        found = true;
        break;
      }

      if (found)
        high = mid;
      else
        low = mid;

      //printf("%lf %lf\n", high, low);
    }

    printf("Case #%d: %.8lf\n", ii, low);
  }
}

