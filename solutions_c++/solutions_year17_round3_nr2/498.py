#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

int findBest(vi& d, int start) {
	vvvi mem(1441, vvi(1441, vi(2,1000000)));
	mem[0][0][start] = 0;
	mem[0][0][1-start] = 1;
	for(int t = 1;t <= 1440; ++t) {
		for(int a = 0; a <= t; ++a) {
			for(int p = 0;p < 2; ++p) {
				int tmp = 1000000;
				if((a-(p==0) >= 0) && (t-1 >= a-(p==0)) && d[t] != p) {
					tmp = min(tmp, mem[t-1][a-(p==0)][0] + (p != 0));
					tmp = min(tmp, mem[t-1][a-(p==0)][1] + (p != 1));
				}
				mem[t][a][p] = tmp;
			}
		}
	}
	int best = mem[1440][720][start];
	best = min(best, mem[1440][720][1-start]+1);
	return best;
}

int solve() {
	int ac, aj;
	cin >> ac >> aj;
	vi d(1441,2);
	for(int i = 0;i < ac; ++i) {
		int l,r;
		cin >> l >> r;
		for(int j = l+1;j <= r; ++j) {
			d[j] = 0;
		}
		// cout << "from " << l << " to " << r << ": 0" << endl;
	}
	for(int i = 0;i < aj; ++i) {
		int l,r;
		cin >> l >> r;
		for(int j = l+1;j <= r; ++j) {
			d[j] = 1;
		}
		// cout << "from " << l << " to " << r << ": 1" << endl;
	}
	int best = min(findBest(d,0), findBest(d,1));
	return best;
}

int main() {
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t = 1;t <= T; ++t) {
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}