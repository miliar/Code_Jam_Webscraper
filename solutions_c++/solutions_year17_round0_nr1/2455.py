#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

bool flip[2005]={0};

void op(char& c) {
	c = (c=='-')?'+':'-';
}

int main() {
	ios::sync_with_stdio(0); cin.tie();
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		string s;
		int k,n;
		cin >> s >> k;
		n = s.size();
		fill(flip,flip+n,0);
		bool fl = 0;
		int ans = 0;
		for(int i = 0; i < n; ++i) {
			fl ^= flip[i];
			if(fl) op(s[i]);
			if(i <= n-k) {
				if(s[i] != '+') {
					op(s[i]);
					++ans;
					fl^=1;
					flip[i+k]^=1;
				}
			}
			if(s[i] == '-')
				ans = 0x80000000;
		}
		if(ans < 0) cout << "IMPOSSIBLE\n";
		else cout << ans << "\n";
	}
	return 0;
}