#include <cstring>
#include <iostream>
#include <cmath>

using namespace std;

class Solution {
	string st;
	int n;
	int f[222];
public:

	void flip(int i) {
		for(int j = 0; j < n; j++) {
			st[j + i] = (st[j + i] == '-') ? '+' : '-';
		}
	}

	void solve() {
		int res = 0;
		for(int i = 0; i <= st.size() - n; i++) {
			if (st[i] == '-') {
				res++;
				flip(i);
			}
		}
		for(int i = 0; i < st.size(); i++) {
			if (st[i] == '-') {
				cout << "IMPOSSIBLE" << endl;
				return;
			}
		}
		cout << res << endl;
	}

	void execute()  {
		int test = 0;
		cin >> test;
		for(int t = 1; t <= test; t++) {
			cin >> st >> n;
			cout << "Case #" << t << ": ";
			solve();
		}
	}
};

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	Solution sol;
	sol.execute();
	return 0;
}