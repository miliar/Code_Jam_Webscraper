#include <cstdio>
#include <algorithm>
using namespace std;

const int infinity = 1e9 + 9;

int K;
char S[1009];

void flip(int i) {
  if (S[i] == '+')
    S[i] = '-';
  else
    S[i] = '+';
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%s %d", S, &K);
    
    // compute
    printf("Case #%d:", Ti);
    int num_flips = 0;
    for (int i = 0; i < strlen(S) - K + 1; i++)
      if (S[i] == '-') {
        num_flips++;
        for (int k = 0; k < K; ++k)
          flip(i+k);
      }

    // output
    bool ok = true;
    for (int i = strlen(S) - K + 1; i < strlen(S); ++i)
      if (S[i] != '+') {
        ok = false;
        break;
      }
    if (ok)
      printf(" %d", num_flips);
    else
      printf(" IMPOSSIBLE");
    printf("\n");
  }
  return 0;
}
