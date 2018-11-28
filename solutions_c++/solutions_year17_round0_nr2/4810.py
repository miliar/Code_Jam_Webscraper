#include <cstdio>
#include <algorithm>
using namespace std;

const int infinity = 1e9 + 9;

char N[29];

int main()
{
  int T;
  scanf("%d ", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf(" %s", N);
    
    // try to preserve as much as possible from the number
    int L = strlen(N);
    for (int i = L; i >= 0; --i) {
      // cannot preserve due to lack of "upward jump"
      if ((i > 0) && (i < L) && (N[i-1] >= N[i]))
        continue;

      // check i-prefix is non-decreasing
      bool ok = true;
      for (int j = 0; j < i-1; ++j)
        if (N[j] > N[j + 1]) {
          ok = false;
          break;
        }
      if (!ok)
        continue;

      // if checks passed, construct the result and exit
      // printf("Decreasing at i=%d from N[i]=%c\n", i, N[i]);
      if (i < L)
        N[i]--;
      for (int j = i + 1; j < L; ++j)
        N[j] = '9';
      break;
    }

    // output
    printf("Case #%d: ", Ti);
    if (N[0] > '0')
      printf("%c", N[0]);
    for (int i = 1; i < L; ++i)
      printf("%c", N[i]);
    printf("\n");
  }
  return 0;
}
