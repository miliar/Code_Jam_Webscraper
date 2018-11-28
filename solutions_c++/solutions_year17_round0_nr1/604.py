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

const int N = 1<<15;
char buf[N];

void solve(){
	// exact implementation appears here
	int K;
	scanf("%s%d",buf,&K);
	int len = strlen(buf);

	int ans = 0;
	int i = 0;
	for(i=0;i <= len-K; ++i) {
		if(buf[i] == '-') {
			for(int j=i; j<i+K; ++j){
				char c = buf[j];
				buf[j] = c =='-' ? '+' : '-';
			}
			++ans;
		}
	}

	while(i < len) {
		if(buf[i] == '-') {
			ans = -1;
			break;
		}
		++i;
	}

	if(ans < 0) puts("IMPOSSIBLE");
	else printf("%d\n", ans);

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
