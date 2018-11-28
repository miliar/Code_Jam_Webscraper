#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>

#define mp make_pair
#define pb push_back


typedef long long ll;
typedef long double ld;

using namespace std;

#ifndef LOCAL
#define cerr _cer
struct _cert
{
    template <typename T> _cert& operator << (T) { return *this; }
};
_cert _cer;
#endif

template <typename T> void dprint(T begin, T end) {
    for (auto i = begin; i != end; i++) {
		cerr << (*i) << " ";
    }
    cerr << "\n";
}
string s;
int k;
int en[12000];
int n;

void solve() {
	cin >> s >> k;
	n = s.size();
	int ans = 0;
	int now = 0;
	for (int i = 0; i < n; ++i)
		en[i] = 0;
	for (int i = 0; i <= n - k; ++i) {
		int x = 0;
		if (s[i] == '+')
			x = 1;
		x ^= now;
		if (x == 0) {
			en[i] = 1;
			now ^= 1;
			++ans;
		}
		if (i >= k - 1 && en[i - (k - 1)])
			now ^= 1;
	}
	for (int i = n - k + 1; i < n; ++i) {
		int x = 0;
		if (s[i] == '+')
			x = 1;
		x ^= now;
		if (x == 0) {
			cout << "IMPOSSIBLE\n";
			return;
		}
		if (i >= k - 1 && en[i - (k - 1)])
			now ^= 1;
	}
	cout << ans << "\n";
}

int main() {
	int tt;
	cin >> tt;
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}


