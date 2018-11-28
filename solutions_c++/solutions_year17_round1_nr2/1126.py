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


bool Match(const std::vector<long long int> &R, const long long int Q0,
           const long long int Q1)
{

        int q = Q0;
        int r = R[0];
        int x1 = (10 * q + 11 * r - 1) / (11 * r);
        int x2 = (10 * q ) / (9 * r);

        q = Q1;
        r = R[1];
        int y1 = (10 * q + 11 * r - 1) / (11 * r);
        int y2 = (10 * q ) / (9 * r);

        //printf("%d %d %d %d\n", x1, x2, y1, y2);
        if (x1 <= y2 && y1 <= x2) return true;
        return false;
}

int Count(const std::vector<int> &X, const std::vector<long long int> &R,
          const std::vector<std::vector<long long int>> &Q)
{
  int c = 0;
  for (int i = 0; i < X.size(); ++i)
  {
    bool match = Match(R, Q[0][i], Q[1][X[i]]);
    if (match) ++c;
  }

  return c;
}

int main()
{
  int T; scanf("%d\n", &T);
  for (int ii = 1; ii <= T; ++ii)
  {
    long long int N, P; scanf("%lld %lld\n", &N, &P);
    std::vector<long long int> R(N);
    for (int i = 0; i < N; ++i) scanf("%lld", &R[i]);

    std::vector<std::vector<long long int>> Q(N, std::vector<long long int>(P));
    for (int i = 0; i < N; ++i) for (int j = 0; j  <P; ++j)
      scanf("%lld", &(Q[i][j]));

    int mmx = 0;
    if (N == 1)
    {
      for (int i = 0; i < P; ++i)
      {
        int q = Q[0][i];
        int r = R[0];

        int x1 = (10 * q + 11 * r - 1) / (11 * r);
        int x2 = (10 * q ) / (9 * r);
        if (x1 <= x2) mmx++;
      }
    }
    else
    {
      std::vector<int> X(P);
      for (int i = 0; i < P; ++i) X[i] = i;
      do
      {
        int c = Count(X, R, Q);
        if (mmx < c) mmx = c;
      } while (std::next_permutation(X.begin(), X.end()));
    }

    printf("Case #%d: %d\n", ii, mmx);
  }
}
