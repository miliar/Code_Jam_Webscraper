#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    int N, P;
    scanf("%d %d", &N, &P);
    int temp;
    int answer = 0;
    if(P == 2) {
      int x0 = 0;
      int x1 = 0;
      for(int i = 0; i < N; ++i) {
        scanf("%d", &temp);
        if(temp % 2 == 1) {
          x1++;
        } else {
          x0++;
        }
      }

      // compute
      answer = x0 + (x1 / 2);
      if(x1 % 2 == 1) {
        answer++;
      }
    } else
    if(P == 3) {
      int x0 = 0;
      int x1 = 0;
      int x2 = 0;
      for(int i = 0; i < N; ++i) {
        scanf("%d", &temp);
        if(temp % 3 == 1) {
          x1++;
        } else 
        if(temp % 3 == 2) {
          x2++;
        } else {
          x0++;
        }
      }

      int y = min(x1, x2);
      int z = max(x1, x2) - y;

      answer = x0 + y + (z / 3);
      if(z % 3 != 0) {
        answer++;
      }
      // compute
    } else
    if(P == 4) {
      int x0 = 0;
      int x1 = 0;
      int x2 = 0;
      int x3 = 0;
      for(int i = 0; i < N; ++i) {
        scanf("%d", &temp);
        if(temp % 4 == 1) {
          x1++;
        } else 
        if(temp % 4 == 2) {
          x2++;
        } else
        if(temp % 4 == 3) {
          x3++;
        } else {
          x0++;
        }
      }

      // compute
    }
    printf("Case #%d: %d\n", t, answer);
  }
}