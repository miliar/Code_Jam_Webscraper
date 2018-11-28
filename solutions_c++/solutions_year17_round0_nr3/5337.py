#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <stack>
#include <queue>
using namespace std;

int main() {
  int TC;
  scanf("%d", &TC);
  for(int t = 1; t <= TC; ++t) {
    long long int N, K;
    scanf("%lld %lld", &N, &K);

    long long int A = pow(2, floor(log2(K)));
    long long int B = K-A+1;;
    long long int P = N-A+1;
    long long int Q = P / A;
    long long int R = P % A;

    long long int ans = Q;
    if(B <= R) {
      ans++;
    }
    ans--;

    printf("Case #%d: %lld %lld\n", t, (ans / 2) + (ans % 2), ans / 2);
  } 
}