#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string.h>
#include <functional>
#include <utility>
using namespace std;

const int infi = 2147483646;
const int null = -2147483646;

const int N = 9999;

char pan[N];

int main(){
  freopen("A-large.in","r",stdin);
  freopen("out.txt","w",stdout);

  int cases;
  cin >> cases;

  for (int q = 1; q <= cases; q++) {
    printf("Case #%d: ", q);
    scanf("%s", pan);

    int sz = strlen(pan);

    int k;
    scanf("%d", &k);

    int ans = 0;

    // solution
    for (int i = sz-1; i > 0; i--) {
      if (pan[i] == '-') {
        for (int j = i; j > i-k; j--) {
          if (j < 0) {
            ans = -1;
            goto stop;
          }
          if (pan[j] == '-') {
            pan[j] = '+';
          } else {
            pan[j] = '-';
          }
        }
        ans++;
      }
    }

    // output
    stop:

    if (pan[0] != '-' && ans >= 0) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
}
