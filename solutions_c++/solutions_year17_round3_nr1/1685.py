#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;
const double PI  = 3.141592653589793238463;

double solve() {
  int K,N;
  cin >> N >> K;
  vector<long long> r;
  vector<long long> h;
  r.resize(N);
  h.resize(N);
  for(int i=0;i<N;i++) {
    cin >> r[i] >> h[i];
  }
  long long maxi = 0;
  for(int i=0;i<N;i++) {
    long long s = 0;
    s += r[i]*r[i];
    s += 2*r[i]*h[i];
    vector<long long> v;
    for(int j=0;j<N;j++) {
      if(j==i)continue;
      if(r[j] <= r[i]) {
        v.push_back(-2*r[j]*h[j]);
      }
    }
    if(v.size() < K - 1) continue;
    sort(v.begin(), v.end());
    for(int j = 0;j<K-1;j++) {
      s += -v[j];
    }
    if(s > maxi)
      maxi = s;
  }
  return maxi * PI;
}


int main() {
  int T;
  scanf("%d", &T);
  for(int t=1;t<=T;t++) {
    printf("Case #%d: %lf\n", t, solve());
  }
}
