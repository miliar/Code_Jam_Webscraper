#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

typedef vector<int> vi;

int solve() {
	int n,k;
	string s;
	cin >> s;
	cin >> k;
	n = (int)s.length();
	vi xs(n);
	for(int i = 0;i < n;++i) {
		xs[i] = s[i] == '+';
	}
	int flips = 0;
	for(int i = 0;i+k <= n;++i) {
		if(xs[i] == 0) {
			++flips;
			for(int j = i;j < i+k; ++j) {
				xs[j] = 1-xs[j];
			}
		}
	}
	for(int i = 0;i < n; ++i) {
		if(xs[i] == 0) return -1;
	}
	return flips;
}

int main() {
	int T;
	cin >> T;
	for(int t = 1;t <= T;++t) {
		int s = solve();
		cout << "Case #" << t << ": ";
		if(s == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << s;
		}
		cout << endl;
	}
}