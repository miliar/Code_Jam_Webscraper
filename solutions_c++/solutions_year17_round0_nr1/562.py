#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

bool b[2000];

void solve() {
	string s;
	int n;
	cin >> s >> n;
	// cout << s.length() << " " << n ;
	int m = s.length();
	for (int i = 0; i < m; ++i )
		b[i] = (s[i]=='-');
	int ans = 0;
	for (int i = 0; i <= m-n; ++i ) { // [0,...,m-1], [m-n...,m-1]
		ans += b[i];
		if (b[i]) {
			for (int j = 0; j < n; ++j ) 
				b[i+j] ^= 1;
		}
	}
	for (int i = m-n+1; i < m; ++i ) {
		if (b[i]) {
			cout << "IMPOSSIBLE";
			return;
		}
	}
	cout << ans;
}

int main(int argc, char *argv[]) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	cin >> testNum;
	for (int testid = 0; testid < testNum; ++testid ) {
		cout << "Case #" << testid+1 << ": ";
		solve();
		cout << endl;
	}
}