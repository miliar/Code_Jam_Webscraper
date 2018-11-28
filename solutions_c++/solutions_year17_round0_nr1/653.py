#include <stdio.h>
#include <string>

int swap[1024];

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    char buff[1024];
    scanf("%s\n", &buff);
    std::string str(buff);
    int N;
    scanf("%d\n", &N);
    int count = 0;
    int rcount = 0;
    for (int i = 0; i < str.size(); i++) {
      if (i >= N) {
        rcount -= swap[i - N];
      }
      int val = str[i] == '-';
      val += rcount % 2;
      if (val % 2 == 1) {
        if (i + N > str.size()) {
          count = -1;
          break;
        }
        count++;
        rcount++;
        swap[i] = 1;
      } else {
        swap[i] = 0;
      }
    }
    if (count == -1) {
      printf("Case #%d: IMPOSSIBLE\n", t);
    } else {
      printf("Case #%d: %d\n", t, count);
    }
  }
}