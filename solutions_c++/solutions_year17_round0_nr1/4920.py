#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

int main()
{
  int T; scanf("%d\n", &T);
  for (int ii = 1; ii <= T; ++ii)
  {
    char S[1005];
    int K;
    scanf("%s %d\n", S, &K);

    int x = 0;
    int L = strlen(S);
    for (int i = 0; i + K <= L; ++i)
    {
      if (S[i] == '-')
      {
        ++x;
        for (int j = 0; j < K; ++j)
        {
          if (S[i+j] == '-') S[i+j] = '+';
          else S[i+j] = '-';
        }
      }
    }

    bool possible = true;
    for (int i = 0; i < L; ++i) if (S[i] == '-') possible = false;

    if (possible)
      printf("Case #%d: %d\n", ii, x);
    else
      printf("Case #%d: IMPOSSIBLE\n", ii);
  }
}
