#include <cstdio>
#include <cstring>

char buffer[1001];

int main() {
  int N;
  scanf("%d", &N);
  for (int k = 0; k < N; k++) {
    int K;
    int M;
    int S = 0;
    scanf("%s", buffer);
    M = strlen(buffer);
    scanf("%d", &K);
    int s = M - K + 1;
    for (int i = 0; i < s; i++) {
      if (buffer[i] == '-') {
        S++;
        for (int j = i; j < i+K; j++) {
          switch(buffer[j]) {
            case '-': buffer[j] = '+'; break;
            case '+': buffer[j] = '-'; break;
          }
        }
      }
    }
    bool p = true;
    for (int i = s; p && i < M; i++) {
      if (buffer[i] == '-') { p = false; }
    }
    printf("Case #%d: ", k+1);
    if (p) printf("%d", S);
    else printf("IMPOSSIBLE");
    printf("\n");
  }
  return 0;
}
