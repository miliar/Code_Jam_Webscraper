#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#ifdef OLYMP_HXLOCAL
	#define P(expr) (cerr << "[line " << __LINE__ << "] " << #expr << ": " << expr << '\n')
#else
	#define P(expr)
#endif

#define len(arr) ((int)(arr).size())

typedef long long ll;

void solve() {
    ll N, K;
    cin >> N >> K;

    map<ll, ll> segments = {{N, 1}};
    ll filled = 0;
    while (!segments.empty()) {
        auto it = --segments.end();
        ll length = it->first;
        ll count = it->second;
        segments.erase(it);

        ll L_s = (length - 1) / 2;
        ll R_s = length / 2;
        if (filled + count >= K) {
            cout << max(L_s, R_s) << ' ' << min(L_s, R_s) << '\n';
            return;
        }
        filled += count;

        if (L_s > 0)
            segments[L_s] += count;
        if (R_s > 0)
            segments[R_s] += count;
    }
    assert(false);
}

int main() {
#ifndef OLYMP_HXLOCAL
	cin.tie(0);
	ios_base::sync_with_stdio(false);
#endif

	int T;
    cin >> T;
    for (int no = 1; no <= T; no++) {
		cout << "Case #" << no << ": ";
		solve();
	}
	return 0;
}

