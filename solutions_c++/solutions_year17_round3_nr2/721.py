
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include "boost/multi_array.hpp"

#define rep(i,n) for (int (i)=0; (i) < (n); ++(i))
#define repf(i,a,b) for (int (i)=(a); (i) <= (b); ++(i))

using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector< vd > vdd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;

const double PI = acos(-1);

int main() {
  int T;
  cin >> T;
  repf (tc,1,T) {
    int ac, aj;
    cin >> ac >> aj;
    vpii act1(ac), act2(aj);
    rep(i,ac) cin >> act1[i].first >> act1[i].second;
    rep(j,aj) cin >> act2[j].first >> act2[j].second;

    vector<bool> must_care(1441,false), must_free(1441,false);
    rep(i,ac) {
      repf(j, act1[i].first, act1[i].second-1) must_free[j] = true;
    }
    rep(i, aj) {
      repf(j, act2[i].first, act2[i].second-1) must_care[j] = true;
    }

    boost::multi_array<int,3> dp(boost::extents[1441][721][2]);
    rep(p,2) {
      //rep(k,721) dp[0][k][p] = 2000; //inf
      dp[0][0][p] = 0;
    }
    repf(n,1,1440) {
      repf(k,0,720) {
        rep(p, 2) {
          dp[n][k][p] = 2000; //inf
          if (!must_free[n] && k>0) {
            //a minute of care for the guy is valid
            dp[n][k][p] = min(dp[n][k][p], (1-p) + dp[n-1][k-1][1]);
          }
          if (!must_care[n] && n>k) {
            //a minute of care for the woman is valid
            dp[n][k][p] = min(dp[n][k][p], p + dp[n-1][k][0]);
          }
        }
      }
    }
    cout << "Case #" << tc << ": ";
    rep(p,2) {
      if (dp[1440][720][p] & 1) dp[1440][720][p]++;
    }    
    cout << min(dp[1440][720][0],dp[1440][720][1]) << endl;
    //cout << dp[1440][720][0] << " " << dp[1440][720][1] << endl;
  }
}
