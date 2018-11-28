#include <cstdio>
#include <cstring>

int main() {
  int T;
  scanf("%d", &T);
  for (int TT = 0; TT < T; TT++) {
    char N[21];
    scanf("%s", N);
    int n = strlen(N);
    while (true) {
      // check
      int j; // hanyadik az elso nem stimmelo
      for (j = 1; j < n; j++) {
        if (N[j-1] > N[j]) break;
      }
      if (j == n) break; // ok
      if (j == 1 && N[0] == '1') {
        for (int i = 1; i < n; i++) {
          N[i-1] = '9';
        }
        N[n-1] = 0;
        break;
      }
      N[j-1]--;
      for (int i = j; i < n; i++) {
        N[i] = '9';
        }
    }
    printf("Case #%d: %s\n", TT+1, N);
  }
}
