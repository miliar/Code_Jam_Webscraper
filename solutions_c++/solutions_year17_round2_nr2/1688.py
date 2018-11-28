#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;

class ahash{
public:
	long operator()(const pair<u16string, int> &a) const {
		hash<u16string> h1;
		return h1(a.first) ^ (0x9e3779b9 + a.second);
	}
};

int N;
const string cols = "ROYGBV";
unordered_map<pair<u16string, int>, bool, ahash> dp;
vector<int> sol;
bool solve(u16string colour, int last) {
//	cout << sol.size() << endl;
	if (sol.size() == N) {
		return 1;
	}
	int big = 0, sum = 0;
	for (int i = 0; i < 6; i++) {
		if (colour[i] > big)
			big = colour[i];
		sum += colour[i];
	}
	if (big > sum - big + 5)
		return dp[{colour, last}] = 0;
	if (dp.count({colour, last})) {
//		cout << "dp'ed" << endl;
		return dp[{colour, last}];
	}
	for (int i = last + 2; i < last + 5; i++) {
		if (colour[i%6]) {
			colour[i%6]--;
			sol.push_back(i%6);
			if (sol.size() == N) {
				if (abs(sol[0] - sol[N-1]) <= 1) {
					sol.pop_back();
					colour[i%6]++;
					return dp[{colour, last}] = 0;
				}
			}
			if (solve(colour, i%6)) {
				return 1;
				colour[i%6]++;
				return dp[{colour, last}] = 1;
			}
			sol.pop_back();
			colour[i%6]++;
		}
	}
	return dp[{colour, last}] = 0;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		u16string colour;
		for (int i = 0; i < 6; i++) {
			int k; cin >> k;
			char16_t c = (char16_t) k;
			colour.push_back(c);
		}
		dp.clear();
		sol.clear();
		for (int i = 0; i < 6; i++) {
			if (colour[i]) {
				colour[i]--;
				sol.push_back(i);
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (solve(colour, sol[0])) {
			for (int i : sol)
				cout << cols[i];
			cout << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
//		cout << dp.size() << endl;
	}
	return 0;
}