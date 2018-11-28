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

const int N = 1500;
int C,J;
int dp[N][N][2];
bool busy_C[N];
bool busy_J[N];
//int task_C[N][2];
//int task_J[N][2];


int get_ans(int s) {
  // dp[i][j][s]
  // first i minutes, C takes j minutes,
  // and at the last minute it is s. (s=0 means C)
  for(int i=0;i<N;++i) for(int j=0;j<N;++j){
    dp[i][j][0] = N;
    dp[i][j][1] = N;
  }
  
  dp[0][0][0] = s;
  dp[0][0][1] = 1 - s;
  
  const int H = 720;
  for(int i=1;i<=720; ++i) {
    if( !busy_J[i-1]) {
      dp[i][0][1] =  dp[i-1][0][1];
    }
    if( !busy_C[i-1] ){
      dp[i][i][0] = dp[i-1][i-1][0];
    }
  }
  
  for(int i=1;i<= 1440; ++i) {
    for(int j=1; j<i && j <= 720; ++j){
      // dp[i][j][0]
      if( !busy_C[i-1] ) {
        dp[i][j][ 0 ] = min( dp[i-1][j-1][0], dp[i-1][j-1][1] + 1);
      }
      else {
        // do nothing
      }
      
      // dp[i][j][1]
      if( !busy_J[i-1] ) {
        dp[i][j][ 1 ] = min( dp[i-1][j][1], dp[i-1][j][0] + 1);
      }
    }
  }
  
  return dp[2*H][H][s];
  
  //int ans = min(dp[2*H][H][0] + s, dp[2*H][H][1] + s);
  //return ans;
}


void solve(){
	// exact implementation appears here
	cin >> C >> J;
	vector<pair<int,int>> task_C;
	vector<pair<int,int>> task_J;

	for(int i=0;i<N;++i){
		busy_C[i] = false;
		busy_J[i] = false;
	}
	for(int i=0;i<C;++i) {
		int b,e;
		cin >> b >> e;
		//task_C.push_back( make_pair(b,e) );
		for(int j=b;j<e;++j) busy_C[j] = true;
	}

	for(int i=0;i<J;++i) {
		int b,e;
		cin >> b >> e;
		//task_J.push_back( make_pair(b,e) );
		for(int j=b;j<e;++j) busy_J[j] = true;
	}

	//sort(task_C.begin(), task_C.end());
	//sort(task_J.begin(), task_J.end());

    int ans = min( get_ans(0), get_ans(1) );
	printf("%d\n",ans);
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
