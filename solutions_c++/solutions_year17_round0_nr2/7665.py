#include <bits/stdc++.h>

using namespace std;

const int N = 20;

char str[N];

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    scanf("%s", str);
    int n = strlen(str);
    bool done = false;
    while (done == false) {
      done = true;
      for (int i = 1; i < n; i++) {
        if (done == false) {
          str[i] = '9';
        } else if (str[i] < str[i - 1]) {
          str[i - 1]--;
          str[i] = '9';
          done = false;
        }
      }
    }
    int i = 0;
    while (str[i] == '0') i++;
    printf("%s\n", str + i);
  }
  return 0;
}
