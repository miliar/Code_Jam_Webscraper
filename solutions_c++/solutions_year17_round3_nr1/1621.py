#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<climits>
#include<sstream>
#include<deque>
#include<queue>
#include<sstream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<bitset>

#define REP(i,s,n) for(int i=s;i<n;++i)
#define rep(i,n) REP(i,0,n)
#define EPS (1e-8)
#define equals(a,b) (fabs((a)-(b))<EPS)

using namespace std;

typedef long long ll;

#define MAX 1010
int N,K;
double H[MAX],R[MAX];

bool LT(double a,double b) { return !equals(a,b) && a < b; }
bool LTE(double a,double b) { return equals(a,b) || a < b; }

struct Cake {
  double h,r;
  bool operator < ( const Cake &cake ) const {
    if( !equals(r,cake.r) ) return LT(cake.r,r); // r > cake.r
    return LT(cake.h,h);
  }
};

double sans;
void small() {
  double maxi = 0;
  rep(i,(1<<N)) {
    if( __builtin_popcount(i) != K ) continue;
    vector<Cake> vec;
    rep(j,N) if( ( i >> j ) & 1 ) vec.push_back((Cake){H[j],R[j]});
    sort(vec.begin(),vec.end());
    
    double area = 0;
    rep(j,K) {
      area += ( vec[j].r * vec[j].r * M_PI + 2.0 * M_PI * vec[j].r * vec[j].h );
      if( j - 1 >= 0 ) {
	area -= ( vec[j].r * vec[j].r * M_PI );
      }
    }
    
    if( LT(maxi,area) ) maxi = area;
  }
  printf("%.9f\n",maxi);
  sans = maxi;
}

double lans;
const bool debug = false;
double dp[MAX][MAX];
// dp[今何個？][半径] := 最大値
void large() {
  vector<Cake> cake;
  rep(j,N) cake.push_back((Cake){H[j],R[j]});
  sort(cake.begin(),cake.end());

  if( debug ) {
    rep(i,N) {
      cout << cake[i].r << "," << cake[i].h << endl;
    }
  }

  vector<int> vec;
  rep(i,N) vec.push_back((int)R[i]);
  sort(vec.begin(),vec.end());
  vec.erase(unique(vec.begin(),vec.end()),vec.end());

  if( debug ) {
    cout << "R = " << endl;
    rep(i,(int)vec.size()) cout << i << " : " << vec[i] << endl;
  }

  /*
  rep(i,N+1) rep(j,K+1) dp[i][j] = -1;
  rep(i,K+1) dp[0][i] = 0;
  */
  rep(i,MAX) rep(j,MAX) dp[i][j] = -1;
  rep(i,MAX) dp[0][i] = 0;

  rep(i,N) { // 次にどれを使う?1000
    for(int j=K-1;j>=0;--j) { // 今何個選んだ?1000
      rep(k,(int)vec.size()) { // この時の半径は？1000
	if( LT(dp[j][k],0) ) continue;
	if( LTE(cake[i].r,vec[k]) ) { // cake[i] <= vec[k]
	  double area = dp[j][k];
	  area += ( cake[i].r * cake[i].r * M_PI + 2.0 * M_PI * cake[i].r * cake[i].h );
	  if( j - 1 >= 0 ) {
	    area -= ( cake[i].r * cake[i].r * M_PI );
	  }
	  int id = lower_bound(vec.begin(),vec.end(),cake[i].r,LT) - vec.begin();
	  assert( equals(vec[id],cake[i].r) );
	  if( LT(dp[j+1][id],area) ) {
	    if( debug ) {
	      cout << "update : " << "dp[" << j+1 << "][" << id << "] (" << dp[j+1][id] << ")" << " = " << area <<endl;
	    }
	    dp[j+1][id] = area;

	  }
	}
      }
    }
  }
  double ans = 0;
  rep(i,(int)vec.size()) if( LT(ans,dp[K][i]) ) ans = dp[K][i];
  printf("%.9f\n",ans);
  lans = ans;
}

int main() {
  int T,CNT=1;
  cin >> T;
  while( T-- ) {
    cout << "Case #" << CNT++ << ": ";
    cin >> N >> K;
    rep(i,N) cin >> R[i] >> H[i];
    //small();
    large();
    /*
    if( !equals(sans,lans) ) {
      if( N == 3 ) {
	cout << N << " " << K << endl;
	rep(i,N) {
	  cout << R[i] << " " << H[i] << endl;
	}
      }
    }
    */
  }
  return 0;
}
