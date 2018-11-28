#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

vector<int> Digits(long long int N)
{
  vector<int> M;
  while (N > 0)
  {
    M.insert(M.begin(), N % 10);
    N = N / 10;
  }

      return M;
}

long long int Create(int D, int n)
{
  long long int s = 0;
  for (int i = 1; i <= D; ++i)
  {
    s *= 10;
    s += n;
  }
  return s;
}

int main()
{
  int T; scanf("%d\n", &T);
  for (int ii = 1; ii <= T; ++ii)
  {
    long long int N; scanf("%lld\n", &N);
    vector<int> M = Digits(N);
    const int D = M.size();

    const long long int Ones = Create(D, 1);
    if (Ones > N)
    {
      const long long int Nines = Create(D-1, 9);
      printf("Case #%d: %lld\n", ii, Nines);
      continue;
    }

    int mxd = 1;
    vector<int> V(D, 1);
    for (int i = 0; i < D; ++i)
    {
      for (int d = mxd; d <= 9; ++d)
      {
        vector<int> W = V;
        for (int j = i; j < D; ++j) W[j] = d;
        bool lc1 = lexicographical_compare(W.begin(), W.end(), M.begin(), M.end());
        bool lc2 = lexicographical_compare(M.begin(), M.end(), W.begin(), W.end());

        if (lc1 || (!lc1 && !lc2))
          V = W;
      }
    }

    printf("Case #%d: ", ii);
    for (int i = 0; i < D; ++i) printf("%d", V[i]);
    printf("\n");
  }
}
