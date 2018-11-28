#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

typedef long long LL;
typedef long double LD;

#define FOR(k,a,b) for(__typeof(a) k=(a); k < (b); ++k)
#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

int solve() {
	int n, p; cin >> n >> p;
	vector<int> g;
	for(int i = 0; i < n; ++i) {
		int x; cin >> x;
		g.push_back(x);
	}
	if (p == 2) {
		int cnt = 0, np = 0;
		FOR(i, 0, n) {
			if (g[i] % 2 == 0) {
				cnt++;
			}
			else {
				np++;
			}
		}
		return cnt + (np + 1)/2;
	}
	if (p == 3) {
		int k[3] = {0, 0, 0};
		FOR(i, 0, n) {
			k[g[i] % 3]++;
		}
		return k[0] + min(k[1], k[2]) + (max(k[1], k[2]) - min(k[1],k[2]) + 2) / 3;
	}
	return 0;
}

int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
		cout << "Case #" << x << ": " << solve() << endl;//result 
	}
	return 0;
}
