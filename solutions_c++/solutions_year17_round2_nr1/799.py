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

void solve(){
	// exact implementation appears here

  long long D;
  int N;

  cin >> D >> N;

  double h = 0;
  for(int i=0;i<N;++i) {
    long long K, S;
    cin >> K >> S;
    
    long long left = D - K;
    double t = (double) left / (double) S;

    if (h < t) {
      h = t;
    }
  }

  double ans = (double) D / h;

  printf("%.6f\n", ans);
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
