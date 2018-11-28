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
	LL N, K;
	cin >> N >> K;
	map<LL,LL> sticks;

	LL B = -1;

	sticks[ N ] = 1;
	while( true ) {
		LL sum  = 0;
		LL max_key = -1, ct = 0; 
		
		for(auto pr : sticks) {
			//std::cout << "len: " << pr.first << "  count: " << pr.second << std::endl;
			sum += pr.second;
			if(max_key < pr.first) {
				max_key = pr.first;
				ct = pr.second;
			}
		}

		//std::cout << std::endl;

		// assume sum - 1 < K

		// find longest one to break
		if (sum -1 + ct >= K) {
			B = max_key;
			break;
		}

		auto it = sticks.find(max_key);
		sticks.erase(it);

		LL part1 = max_key >> 1;
		LL part2 = max_key - part1 -1;
		
		sticks[ part1 ] += ct;
		sticks[ part2 ] += ct;
	}

	// the K-th one will break a stick with length B
	std::cout << (B/2)  << " "<< ( B - 1 - (B/2) ) << std::endl;

	//if(B % 2) std::cout << B/2 << " " << B/2 << std::endl;
	//else {
	//	std::cout << B/2 << " " << (B-1)/2 << std::endl;
	//}
	
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
