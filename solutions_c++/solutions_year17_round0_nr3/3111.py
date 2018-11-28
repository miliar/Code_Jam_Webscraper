#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <unordered_map>
#include <set>
#include <stack>
#include <bitset>
#include <queue>
#include <numeric>
#include <map>
#include <list>
#include <errno.h>
#include <algorithm>
#include <memory>

#include <iterator>
#include <assert.h>
#include <unordered_set>
#include <sstream>

#define pb push_back
#define mp make_pair

//#define x first
//#define y second

using big = long long;

using namespace std;

map<big, big> f;

void solve() {
	f.clear();
	big n, k;
	cin >> n >> k;
	f[n] = 1;
	big mn, mx;
	int cnt = 0;
	while (k > 0) {
		++cnt;
		auto tmp = *f.rbegin();
		f.erase(tmp.first);
		k -= tmp.second;
		big l = tmp.first / 2, r = tmp.first - l - 1;
		mx = max(l, r);
		mn = min(l, r);
		if (l) {
			f[l] += tmp.second;
		}
		if (r) {
			f[r] += tmp.second;
		}
	}
	cout << mx << " " << mn << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		solve();
	}
	fclose(stdin);
	fclose(stdout);
}

