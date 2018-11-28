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

ll n;

void solve() {
	cin >> n;
	vector<int> vv;
	ll tmp = n;
	while (tmp)
		vv.push_back(tmp % 10), tmp /= 10;
	reverse(vv.begin(), vv.end());
	ll now = 0;
	for (int i = 0; i < vv.size(); ++i) {
		int x = vv[i];
		int fl = 0;
		for (int j = i + 1; j < vv.size(); ++j) {
			if (vv[j] > x) {
				fl = 1;
				break;
			}
			else if (vv[j] < x) {
				fl = -1;
				break;
			}
		}
		if (fl == -1) {
			--x;
			now = now * 10 + x;
			for (int j = i + 1; j < vv.size(); ++j)
				now = now * 10 + 9;
			break;
		}
		else {
			now = now * 10 + x;
		}
	}
	cout << now << "\n";
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


