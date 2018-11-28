#include <cstdio>
#include <cstring>

using namespace std;

#define MAXS 1005

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    char S[MAXS];
    scanf(" %s", S);

    int K;
    scanf("%d", &K);

    int N = strlen(S);

    int i = 0;
    int cnt = 0;
    while (i < N) {
      while (i < N && S[i] == '+')
        i++;
      if (S[i] == '-') {
        if (i + K - 1 >= N) {
          cnt = -1;
          break;
        }
        for (int j = i; j <= i + K - 1; j++) {
          if (S[j] == '-')
            S[j] = '+';
          else
            S[j] = '-';
        }
        cnt++;
      }
    }
    printf("Case #%d: ", t);

    if (cnt == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", cnt);
  }

  return 0;
}
