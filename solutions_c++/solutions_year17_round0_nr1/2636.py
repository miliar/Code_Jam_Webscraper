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
inline void case_print() {
	static int it = 0;
	it += 1;
	cout << "Case #" << it << ": ";
}

inline void Solve() {
	string s;
	int k;
	cin >> s >> k;
	//cerr << s << " " << k << endl;
	int counts = 0;
	vector<int> a(s.size() + 2, 0);
	assert(k >= 2 && k <= s.size());
	int add = 0;
	
	for (int i = 0; i <= s.size() - 1; i ++) {
		add += a[i];
		int t = (s[i] == '+' ? 1 : 0);
		t = (t + add) % 2;
		if (i <= s.size() - k && t == 0) {
			counts ++;
			a[i] ++;
			a[i + k] --;
			add ++;
		}
		else {
			if (t == 0) {
				counts = -iinf;
			}
		}
	}
	case_print();
	if (counts < 0) 
		cout << IMPOSSIBLE;
	else
		cout << counts << "\n";
}

int main() {
	ios_base::sync_with_stdio(0);
	freopen("A-large.in", "r",stdin);
	freopen("output.txt", "w", stdout);
	
	int T;
	cin >> T;
	while (T --> 0) {
		Solve();
	}
	
	return 0;
}
