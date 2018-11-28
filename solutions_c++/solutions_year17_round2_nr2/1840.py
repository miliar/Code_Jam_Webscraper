#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <random>

using namespace std;
typedef unsigned long long ull;

random_device rd;
mt19937 rng(rd());
uniform_int_distribution<int> uni(0,5);

void solve() {
	int colors[6];
	int tmpColors[6];
	int n;
	cin >> n;
	for(int i=0; i<6; ++i) {
		cin >> colors[i];
		tmpColors[i] = colors[i];
	}

	// For one color
	for (int i=0; i<6; ++i) {
		if (colors[i] > n/2) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}



	string ans = "";
	for (int x = 0; x<6; ++x) {
		for(int i=0; i<6; ++i) colors[i] = tmpColors[i];
		if (colors[x] == 0) continue;
		ans = "";
		ans += "ROYGBV"[x];
		colors[x]--;
		int last=x;
		for (int i=0; i<n-1; ++i) {
			int max = 0, val = -1;
			for (int c=0; c<6; ++c) {
				int pos = c;
				if (pos==last) continue;
				if (colors[pos] > val) {
					max = pos;
					val = colors[pos];
				}
				
			}
			ans += "ROYGBV"[max];
			--colors[max];
			last = max;
		}
		bool okay = true;
		for (int i=0; i<n; ++i) {
			if (ans[i] == ans[(i+1)%n]) okay = false;
		}
		if (okay) {
			cout << ans << endl;
			return;
		}
	}
	cout << "FAIL" << endl;
}

int main() {
	int cases;
	cin >> cases;
	for (int i=1; i<=cases; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
