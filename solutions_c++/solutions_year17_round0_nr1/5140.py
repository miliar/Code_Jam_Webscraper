#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
using namespace std;

int table[1005];

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    string S;
    int K;
    cin >> S >> K;
    int N = S.length();
    for(int i = 0; i < N; ++i) {
      if(S.substr(i, 1) == "+") {
        table[i] = 1;
      } else {
        table[i] = 0;
      }
    }

    int ans = 0;
    for(int i = 0; i <= N-K; ++i) {
      if(table[i] == 0) {
        ans++;
        for(int j = i; j < i+K; ++j) {
          table[j] = (table[j] + 1) % 2;
        }
      }
    }

    bool logic = true;
    for(int i = N-K+1; i < N; ++i) {
      if(table[i] == 0) {
        logic = false;
        break;
      }
    }

    printf("Case #%d: ", t);
    if(logic) {
      printf("%d\n", ans);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
}