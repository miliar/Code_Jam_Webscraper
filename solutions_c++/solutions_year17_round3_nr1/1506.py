/*************************************************************************
     File Name: a-small.cpp
     ID: obsoles1
     PROG: 
     LANG: C++ 
     Mail: 384099319@qq.com 
     Created Time: Sun 30 Apr 2017 04:51:00 AM EDT
 ************************************************************************/
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 1010;
struct node {
  double r, h;
  bool operator < (const node & rhs) const {
    return 2*r*h > 2*rhs.r*rhs.h;
  }
} a[N];

int main() {
  int t, n, k, i;
  freopen("A-large.in","r",stdin);
  freopen("a-small.out", "w", stdout);
  scanf("%d", &t);
  for (int case_num = 1; case_num <= t; ++case_num) {
    printf("Case #%d: ", case_num);
    scanf("%d%d", &n, &k);
    for (i = 0; i < n; ++i) {
      scanf("%lf%lf", &a[i].r, &a[i].h);
    }
    sort(a, a + n);
    double ans = 0;
    double max_r = 0;
    for (i = 0; i < k - 1; ++i) {
      max_r = max(max_r, a[i].r);
      ans += 2.0*a[i].r*a[i].h;
    }
    double res = ans;
    for (i = k - 1; i < n; ++i) {
      double tmp = max(max_r, a[i].r);
      res = max(res, ans + 2.0*a[i].r*a[i].h + tmp*tmp);
    }
    printf("%lf\n", res*M_PI);
  }
}
