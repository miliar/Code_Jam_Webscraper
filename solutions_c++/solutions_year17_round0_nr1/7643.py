#include <iostream>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

int main() {
  int T;

  scanf("%d\n", &T);

  for (int t = 1; t <= T; t++) {
    char s[1001]; int k;
    for (int i = 0; i < 1001; i++) s[i] = '\0';

    scanf("%s %d\n", s, &k);

    int flips = 0;
    for (int i = 0; s[i+k-1] != '\0'; i++) {
      if (s[i] == '-') {
        flips++;
        for (int j = i; j < i+k; j++){
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
      }
    }

    bool f = true;
    for (int i = 0; s[i] != '\0'; i++) {
      if (s[i] == '-') {
        f = false;
      }
    }
    if (f)
      printf("Case #%d: %d\n", t, flips);
    else
      printf("Case #%d: IMPOSSIBLE\n", t);
  }

  return 0;
}
