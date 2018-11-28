#include <cstdio>
#include <iostream>

using namespace std;

struct oneh
{
  int k, s;
}h[100000];

int cmp(oneh x, oneh y) {
  return x.k<y.k;
}

int T, D,N;
double ans;

int main() {
  cin >> T;
  for (int t = 1;t<=T; t++) {
    cin >> D >>N;
    for (int i=0;i<N; i++) 
      cin>>h[i].k>>h[i].s;
    sort(h, h+N, cmp);
    ans = (double) (D-h[N-1].k) / h[N-1].s;
    for (int i=N-1;i>=0;i--) {
      double it = (double) (D-h[i].k) / h[i].s;
      if (it > ans) {
        ans = it;
      }
    }
    ans = D / ans;
    printf("Case #%d: %f\n",t,ans);
  }
  return 0;
}