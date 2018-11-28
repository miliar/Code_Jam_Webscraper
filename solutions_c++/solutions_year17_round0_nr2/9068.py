#include <cstdio>

// 332 329 299

char num[20];

void solve() {
  scanf("%s", num);

  while(true) {
    bool comp = true;
    // find first pair of desending pair of numbers
    for(int i = 0; num[i+1] != '\0'; ++i) {
      int x = num[i] - '0';
      int y = num[i+1] - '0';

      if(x > y) {
        num[i] = x - 1 + '0';

        for(int j = i + 1; num[j] != '\0'; ++j) {
          num[j] = 9 + '0';
        }
        comp = false;
        break;
      }
    }
    if(comp)
      break;
  }

  for(int i = 0; num[i] != '\0'; ++i) {
    if(num[i] != '0') {
      printf("%s\n", num + i);
      break;
    }
  }

}

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; ++i) {
    printf("Case #%d: ", i);
    solve();
  }
}
