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


const int N = 100;
char buf[N];

void solve(){
	// exact implementation appears here

	scanf("%s", buf);
	int len = strlen(buf);


	// a1 a2 .. an  
	// a1-1  9 9 9 9 9 9 
	// a1 a2 ... ai-1 9 . . . 9

	int i = 0;
	while(i < len) {
		int j = i + 1;
		while(j < len && buf[j] == buf[i]) ++j;

		if(j == len) break;

		if(buf[j] > buf[i]) {
			i = j;
			continue;
		}

		// buf[j] must be less than buf[i]
		buf[i] = buf[i] - 1;
		j = i + 1;
		while(j < len){
			buf[j] = '9';
			++j;
		}
		break;
	}

	if(buf[0] == '0') puts(buf+1);
	else puts(buf);
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
