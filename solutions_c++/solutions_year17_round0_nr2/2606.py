#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>

#define _CRT_SECURE_NO_WARNINGS

using namespace std;

#define iinf 2000000000
#define linf 2000000000000000000LL
#define MOD (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)

const string IMPOSSIBLE = "IMPOSSIBLE\n";
inline void case_print(long long x) {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": " << x << "\n";
}

inline void Solve() {
	long long N;
	cin >> N;
	if (N < 10) {
		return (void(case_print(N)));
	}
	vector<int> digs;
	for (long long x = N; x > 0; x /= 10) {
		digs.push_back(x % 10);
	}
	digs.push_back(0);
	reverse(digs.begin(), digs.end());
	assert(digs.size() >= 3);
	
	int it = 1;
	while (it < digs.size() && digs[it] >= digs[it - 1]) it ++;
	cerr << "IT = " << it << endl;
	if (it == digs.size())
		return void(case_print(N));
	it --;
	
	while (it > 0) {
		if (digs[it] > digs[it - 1]) {
			digs[it] --;
			for (int j = it + 1; j < digs.size(); j ++)
				digs[j] = 9;
			break;
		}
		else {
			assert(digs[it] == digs[it - 1]);
			it --;
		}
	}
	assert(it > 0);
	long long result = 0;
	for (int i = 0; i < digs.size(); i ++)
		result = (result * 10ll + digs[i]);
	return void(case_print(result));
}

int main() {
	ios_base::sync_with_stdio(0);
	freopen("B-large.in", "r",stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	while (T --> 0) {
		Solve();
	}
	
	return 0;
}
