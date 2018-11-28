#include "bits/stdc++.h"

#define EPS 1E-9

using namespace std;

using ll = long long;

vector<pair<ll,ll>>v;

bool check(double mid, ll d) {

  for(auto &p: v) {
    if(p.second >= mid) continue;
    double tmp = ((mid) / (mid-p.second))*p.first;
    if( tmp < d) return false;
  }
  return true;
}

int main(int argc, char const *argv[])
{
  freopen("AS.in", "r", stdin);
  freopen("AS.out", "w+", stdout);

  int tcase,cas=1;

  cin>>tcase;

  while(tcase--) {
    ll d,n;
    cin>>d>>n;
    v = std::vector<pair<ll,ll>>(n);

    for(auto &p: v) {
      cin>>p.first>>p.second;
    }

    double low = 1.0;
    double high = 1E15;
    int cnt = 10000;
    while(fabs(high - low) > EPS && cnt--) {
      double mid = (low+high) / 2.0;

      if(check(mid, d)) {
        low = mid;
      } else high = mid;
    }
    printf("Case #%d: %.07lf\n",cas++,low);
  }
  return 0;
}