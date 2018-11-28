#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;
int n,k;
vector<pair<double, double> > rh; 
double dp[1001][1001];


double solve(int ci, int lf) {
  double & ret = dp[ci][lf];
  if(ret!=-1) return ret;
  if (lf == 0) return ret = 0;
  if (ci == n) return ret = 0;
  if (n-ci < lf) return ret = 0;
  double rr = rh[ci].first;
  double he = rh[ci].second;
  ret = 2 * rr * he;
  double nxt = 0;
  for(int j=ci+1;j<n;j++) {
    nxt = max(nxt, solve(j, lf - 1));
  }
  return ret = ret + nxt;
}

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    for(int i=0;i<1001;i++) for(int j=0;j<1001;j++) dp[i][j] = -1;
    cin >> n >> k;
    rh.clear();
    rh = vector<pair<double, double> > (n);
    for(int i=0;i<n;i++) {
      double x,y;
      cin >> x >> y;
      rh.push_back(make_pair(x,y));
    }
    sort(rh.begin(), rh.end());
    reverse(rh.begin(), rh.end());
    double ret = 0;
    for(int i=0;i<n;i++) {
      double rr = rh[i].first;
      ret = max(ret, solve(i, k) + rr * rr);
    }
    ret = ret * M_PI;

    printf("Case #%d: ",tc);
    printf("%.7f\n", ret);
  }

  return 0;
}