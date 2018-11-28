#include <iostream>
#include <cstdio>

#define LL long long

using namespace std;

int a[100];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("answer.txt", "w", stdout);
  int  T;
  cin>>T;
  for (int _ = 1; _ <= T; _++) {
    string s;
    cin>>s;
    int n = s.length();
    for (int i = 0; i < n; i++)
      a[i] = s[i] - '0';
    for (int k = 0; k < 2 * n; k++) {
      int i;
      for (i = 1; i < n; i++) {
        if (a[i] < a[i - 1]) {
          a[i] = 9;
          a[i-1] --;
          for (int j = n; j > 0; j--) {
            if (a[j] < 0) {
              a[j - 1] --;
              a[j] = 10 - a[i];
            }
          }
          break;
        }
      }
      for (;i < n; i++)
        a[i] = 9;
    }
    printf("Case #%d: ", _);
    int i = 0;
    while (a[i] == 0) i++;
    while (i < n) {
      printf("%d", a[i]);
      i++;
    }
    printf("\n");
  }
}
