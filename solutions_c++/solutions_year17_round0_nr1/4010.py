#include <iostream>
using namespace std;

int main() {
  int T, K, answer, l;
  char S[1005];
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%s %d", S, &K);
    l = strlen(S);
    answer = 0;
    bool isPossible = true;
    for (int i = 0; i < (l - K + 1); i++) {
      if (S[i] == '-') {
        for (int j = i; j < (i + K); j++) {
          if (S[j] == '-') S[j] = '+';
          else S[j] = '-';
        }
        answer++;
      }
    }
    for (int i = 0; i < l; i++) {
      if (S[i] == '-') {
        isPossible = false;
        break;
      }
    }
    if (isPossible) printf("Case #%d: %d\n", i + 1, answer);
    else printf("Case #%d: IMPOSSIBLE\n", i + 1);
  }
  return 0;
}