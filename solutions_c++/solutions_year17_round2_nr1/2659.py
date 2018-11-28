/*************************************************************************
     File Name: a-small.cpp
     ID: obsoles1
     PROG: 
     LANG: C++ 
     Mail: 384099319@qq.com 
     Created Time: Sat 22 Apr 2017 12:09:20 PM EDT
 ************************************************************************/
#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("a-small.out", "w", stdout);
  int t, i, n;
  double max_t, D, S, K;
  scanf("%d", &t);
  for (int case_num = 1; case_num <= t; ++case_num) {
    printf("Case #%d: ", case_num);
    scanf("%lf%d", &D, &n);
    max_t = 0.0;
    for (i = 0; i < n; ++i) {
      scanf("%lf%lf", &K, &S);
      max_t = max(max_t, (D - K)/S);
    }
    printf("%lf\n", D/max_t);
  }
}
