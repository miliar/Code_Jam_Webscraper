// Author: Xujie Si
// Email: six@gatech.edu
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i,X) for(int i=0;i<(X);++i)
#define PB(X) push_back( (X) )

typedef long long LL;
typedef vector<int> VI;

priority_queue<int> maxQ; // largest on the top
priority_queue<int, VI, greater<int> > minQ; // smallest on the top

auto cmp1 = [](int& a, int& b) -> bool {return a>b;};
auto dbg = ostream_iterator<int>(cerr, ",");

const int N = 110;
double dp[N][N];
LL dis[N][N];
LL L[N];
double S[N];
LL E[N];

double ans[N];

void solve(){
	// exact implementation appears here
  int n, Q;
  cin >> n >> Q;

  for(int i = 0; i< n; ++i) {
    cin >> E[i] >> S[i];
    ans[i] = -1;
  }

  for(int i=0; i < n; ++i) {
    for(int j=0; j < n; ++j) {
      cin >> dis[i][j];
      dp[i][j] = -1.0;
    }
  }

  L[0] = 0;
  for(int i=1; i< n;++i) {
    L[i] = dis[i-1][i] + L[i-1];
  }


  int from,to;
  cin >> from >> to;


  if(from != 1 || to != n) {
    std::cerr << "we are only solving small cases!!! " << std::endl;
    return;
  }

  //dp[0][0] = 0.0;
  ans[0] = 0;
  for(int j = 1; j < n; ++j) {
    for(int i=0; i<j; ++i) {
      if(ans[i] < 0) continue;

      LL t_dis = L[j] - L[i];
      if(t_dis  > E[i] ) {
	continue;
      }
      double t_ans = (double) t_dis / S[i];
      if( ans[j] < 0 || ans[j] > ans[i] + t_ans ) {
	ans[j] = ans[i] + t_ans;
      }
    }    
  }

  if(ans[n-1] < 0) {
    std::cerr << "we reach an impossible solution!!!" << std::endl;
  }
  else{
    printf("%.9lf\n", ans[n-1]);
  }

}

int main()
{
  int cs = 0, T;
  scanf("%d",&T);
  while(++cs <= T){
    printf("Case #%d: ", cs);
    solve();
  }
  return 0;
}
