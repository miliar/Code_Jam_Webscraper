#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {

  int n;
  scanf("%d", &n);

  for (int i = 1; i <= n; i++) {
    char s[1024];
    int k;
    scanf("%s %d", s, &k);

    int sol = 0;
    for (int j = 0; j < strlen(s) - k + 1; j++) {
      if (s[j] == '-') {
        s[j] = '+';
        for (int l = j + 1; l < j + k; l++) {
          s[l] = s[l] == '+' ? '-' : '+';
        }
        sol++;
      }
      
    }

    int imp = 0;
    for (int j = strlen(s) - k; j < strlen(s); j++) {
      if (s[j] == '-') {
        imp = 1;
      }
    }

    if (imp) {
      printf("Case #%d: IMPOSSIBLE\n", i);
    } else {
      printf("Case #%d: %d\n", i, sol);
    }
  }

  return 0;
}
