#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

int A[1005];
int B[1005];

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    for(int i = 0; i <= 1000; ++i) {
      A[i] = 0;
      B[i] = 0;
    }

    int N, C, M;
    scanf("%d %d %d", &N, &C, &M);
    int p, b;
    int a1 = 0;
    int a2 = 0;
    int b1 = 0;
    int b2 = 0;
    int answer = 0;
    for(int i = 0; i < M; ++i) {
      scanf("%d %d", &p, &b);
      if(p == 1 && b == 1) {
        a1++;
        A[p]++;
      } else
      if(p != 1 && b == 1) {
        a2++;
        A[p]++;
      } else
      if(p == 1 && b == 2) {
        b1++;
        B[p]++;
      } else
      if(p != 1 && b == 2) {
        b2++;
        B[p]++;
      }
    }

    answer += a1;
    int bz = max(0, b2-a1);
    answer += b1;
    int az = max(0, a2-b1);
    answer += max(az, bz); 

    int t1 = a1+a2;
    int t2 = b1+b2;
    int x = max(t1, t2);

    int promotion = 0;
    if(answer > x) {
      promotion = 0;
    } else {
      int temporary;
      for(int i = 2; i <= N; ++i) {
        temporary = A[i]+B[i];
        if(temporary > x) {
          promotion = temporary-x;
        }
      }
    }

    printf("Case #%d: %d %d\n", t, answer, promotion);
  }
}